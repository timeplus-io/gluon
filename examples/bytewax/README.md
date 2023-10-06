# Example to Integrate Bytewax and Timeplus together
[timeplus_output.py](https://github.com/timeplus-io/gluon/blob/develop/examples/bytewax/timeplus_output.py) is a Bytewax output/sink for [Timeplus](https://timeplus.com).

Inspired by https://bytewax.io/blog/polling-hacker-news, you can call Hacker News HTTP API with Bytewax and send latest news to Timeplus workspace for SQL-based analysis, such as

```sql
select raw:id as id, raw:by as by, to_time(raw:time) as time, raw:title as title from hn
```

## How to run the demo


```shell
python3.10 -m venv py310-env
source py310-env/bin/activate
#git clone and cd to this gluon/examples/bytewax folder
pip install bytewax
pip install requests 
pip install timeplus

python -m bytewax.run "hackernews:run_hn_flow(0)"
```
It will load ~100 items every 15 second and send the data to Proton.

```python
flow.output("out", TimeplusOutput("https://us.timeplus.cloud","<wsId>","<apiKey>","hn"))
```
`hn` is an example stream name. The `TimeplusOutput` will create the stream if it doesn't exist
```python
class _TimeplusSink(StatelessSink):
    def __init__(self, address: str, workspace_id: str, api_key: str, stream: str):
        self.env=Environment().address(address).apikey(api_key).workspace(workspace_id)
        self.stream=Stream(env=self.env).name(stream)
        if self.stream.exist():
            logger.debug("the stream exists")
        else:
            self.stream.column("raw","string").create()
            logger.debug("new stream created")
```
and batch insert data
```python
    def write_batch(self, items):
        rows=[]
        for item in items:
            rows.append([item]) # single column in each row
        self.stream.ingest(["raw"],rows)
        logger.debug(f"inserting data..")
```

```python
class TimeplusOutput(DynamicOutput):
    def __init__(self, address: str, workspace_id: str, api_key: str, stream: str):
        self.address = address
        self.api_key = api_key
        self.workspace_id = workspace_id
        self.stream=stream

    def build(self, worker_index, worker_count):
        """See ABC docstring."""
        return _TimeplusSink(self.address,self.workspace_id,self.api_key, self.stream)
```
