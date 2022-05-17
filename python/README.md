## Timeplus API Python SDK

Timeplus Python SDK

to install the sdk, run `pip install timeplus`

```python
from rx import operators as ops
from timeplus import Stream, StreamColumn, Query, Env

# initialize timeplus environment
token = os.environ.get("AUTH0_API_TOKEN")
env = (
    Env().schema("https").host("hostname").port("443").token(token)
)
Env.setCurrent(env)

# create a stream
s = (
    Stream()
    .name("stream_name")
    .column(StreamColumn().name("field_name_a").type("string"))
    .column(StreamColumn().name("field_name_b").type("float64"))
)

s.create()

# insert data into stream
s.insert(
    [
        [
            "hello",
            100.1
        ],
        [
            "timeplus",
            20.2
        ],
    ]
)

# delete stream
s.delete()

# run query on existing stream
query = Query().sql(f"select * from stream_name")
query.create()

query.get_result_stream().pipe(ops.take(5)).subscribe(
    on_next=lambda i: print(f"get one query result {i}"),
    on_error=lambda e: print(f"error {e}"),
    on_completed=lambda: query.stop(),
)

```