# Timeplus Python Client

[Timeplus](https://www.timeplus.com/) is a real-time streaming data analytic platform.  Timeplus python client provides basic functionalities to interact with Timeplus cloud, to manage the streaming analytic work loads.


## Installation

Proton Python Driver currently supports the following versions of Python: 3.8, 3.9, and 3.10.

### Installing with pip
We recommend creating a virtual environment when installing Python dependencies. For more information on setting up a virtual environment, see the [Python documentation](https://docs.python.org/3.9/tutorial/venv.html)


```bash
pip install timeplus
```

## 3 API
The `timeplus` python libary supports 3 API:

* [DB API](#db-api) as defined in [Python Database API Specification v2.0](https://peps.python.org/pep-0249/).
* [SQLAchamy](#sqlachamy)
* [REST API](#rest-api)

### DB API

Timeplus python client support DB API defined in [Python Database API Specification v2.0](https://peps.python.org/pep-0249/).  


```python
from timeplus.dbapi import connect

api_key = "your_timeplus_apikey"
api_address = "us.timeplus.cloud"
workspace = "your_timeplus_workspace_id"

# create a connection using host/password/workspace
conn = connect(host=api_address, password=api_key, path=workspace)

# run a streaming query
cursor = conn.execute("select * from car_live_data")

# get first result from the qeury
next_result = cursor.next()

# get next one result from the qeury
row1 = cursor.fetchone()

# get next three result
rows = cursor.fetchmany(3)
```

Note, as the streaming query result is unbounded, the cursor will not end, fetch will be blocked is there is no new query result.


### SQLAchamy

Timeplus python client has implemeted a [SQLAlchemy](https://www.sqlalchemy.org/) dialect to run queries, so user can use it with SQLAlchemy API.

```python
import os
from sqlalchemy import create_engine, text, select, MetaData, Table
from sqlalchemy.dialects import registry

# register timeplus dialect
registry.register("timeplus", "timeplus.sqlalchemy", "TimeplusDialect")

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = "dev.timeplus.cloud"
port = 443
workspace = os.environ.get("TIMEPLUS_WORKSPACE") or "tp-demo"

# create a new engine
engine = create_engine(
    f"timeplus://:{api_key}@{api_address}:{port}/{workspace}")

# execute streaming sql
with engine.connect() as connection:
    result = connection.execute(text("select * from car_live_data"))
    count = 0
    max = 10
    for row in result:
        print(f"got one row : {row}")
        count += 1
        if count >= max:
            break

# execute statement using table from metadata
metadata_obj = MetaData()
car_table = Table(table_name, metadata_obj, autoload_with=engine)
print(f"reflected table is {car_table}")
print(f"cols is {[ (c.name, c.type) for c in car_table.columns]}")

stmt = select(car_table).where(car_table.c.cid == "c00001")
print(stmt)
with engine.connect() as conn:
    count = 0
    max = 3
    for row in conn.execute(stmt):
        print(f"got one row from query {row}")
        count += 1
        if count >= max:
            break
```

### REST API

Timeplus python client also provides resources wrapper which can be used to call the [Timeplus REST API](https://docs.timeplus.com/rest.html) through python object.

here is a list of all supported resources

| Resource              |  Supported Methods                                    |
|-----------------------|--------------------------------------------|
| [Stream](https://docs.timeplus.com/working-with-streams)| create,list,get,delete,ingest,exist        |
| [Query](https://docs.timeplus.com/stream-query)| create,list,get,delete,cancel,analyze      |
| [Source](https://docs.timeplus.com/source) | create,list,get,delete,start,stop          |
| [Sink](https://docs.timeplus.com/destination)| create,list,get,delete,start,stop          |
| [View](https://docs.timeplus.com/view)| create,list,get,delete,exist               |
| [UDF](https://docs.timeplus.com/udf)|  list                                       |
| [Alert](https://docs.timeplus.com/alert)| list                                       |
| [Dashboard](https://docs.timeplus.com/viz#dashboard) | list                                       |


#### query

Run streaming query and fetch the query result with query metrics.

```python
import os
import traceback
import json
from pprint import pprint

from timeplus import Query, Environment

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
workspace = os.environ.get("TIMEPLUS_WORKSPACE")

# Configure API key and address
env = Environment().address(api_address).workspace(workspace).apikey(api_key)

try:
    # list all qeuries
    query_list = Query(env=env).list()
    pprint(f"there are {len(query_list)} queries ")

    # create a new query
    query = (
        Query(env=env).sql(query="SELECT * FROM car_live_data")
        # .batching_policy(1000, 1000)
        .create()
    )

    pprint(f"query with metadata {json.dumps(query.metadata())}")

    # query header is the colume definitions of query result table
    # it is a list of name/value pair
    # for example : [{'name': 'in_use', 'type': 'bool'}, {'name': 'speed', 'type': 'float32'}]
    query_header = query.header()
    pprint(f"query with header {query.header()}")

    # iterate query result
    limit = 3
    count = 0

    # query.result() is an iterator which will pull all the query result in small batches
    # the iterator will continously pulling query result
    # for streaming query, the iterator will not end until user cancel the query
    for event in query.result():
        # metric event return result time query metrics
        # a sample metrics event:
        # {'count': 117, 'eps': 75, 'processing_time': 1560,
        # 'last_event_time': 1686237113265, 'response_time': 861,
        # 'scanned_rows': 117, 'scanned_bytes': 7605}
        if event.event == "metrics":
            pprint(json.loads(event.data))

        # message event contains query result which is an array of arrays
        # representing multiple query result rows
        # a sample message event:
        # [[True,-73.857],[False, 84.1]]
        if event.event == "message":
            pprint(json.loads(event.data))
        count += 1
        if count >= limit:
            break

    query.cancel()
    query.delete()

except Exception as e:
    pprint(e)
    traceback.print_exc()
```

#### stream

Create/list/get/delete of streams

```python
import os
import traceback
import json
from pprint import pprint

from timeplus import Stream, Environment

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
worksapce = os.environ.get("TIMEPLUS_WORKSAPCE")

# Configure API key and address
env = Environment().address(api_address).apikey(api_key).workspace(worksapce)

try:
    # list all streams
    stream_list = Stream(env=env).list()
    pprint(f"there are {len(stream_list)} streams ")

    # create a new stream
    stream = (
        Stream(env=env)
        .name("test")
        .column("time", "datetime64(3)")
        .column("data", "string")
        .create()
    )

    stream_list = Stream(env=env).list()
    pprint(f"there are {len(stream_list)} streams after create")
    pprint(f"created stream is {stream.metadata()}; type is {type(stream.metadata())}")

    a_stream = Stream(env=env).name("test").get()
    pprint(f"get stream is {a_stream.metadata()} ; type is {type(a_stream.metadata())}")

    stream.delete()
    stream_list = Stream(env=env).list()
    pprint(f"there are {len(stream_list)} streams after delete")
except Exception as e:
    pprint(e)
    traceback.print_exc()

```

#### ingest

Ingest data into streams

##### default ingest

```python
stream = (
        Stream(env=env)
        .name("test_ingest")
        .column("time", "datetime64(3)")
        .column("data", "string")
        .create()
    )

stream.ingest(["time", "data"], [[datetime.datetime.now(), "abcd"]])

```

##### ingest json streams

```python
stream = (
        Stream(env=env)
        .name("test_ingest")
        .column("a", "integer")
        .column("b", "string")
        .create()
    )

payload = """
{"a":2,"b":"hello"}
{"a":1,"b":"world"}
"""

stream.ingest(payload=payload, format="streaming")

```

##### ingest one raw event with multiple lines

```python
stream = Stream(env=env).name("test_ingest_raw").column("raw", "string").create()

payload = """
first line
second line
"""

stream.ingest(payload=payload, format="raw")

```

##### ingest multiple lines json

```python
stream = Stream(env=env).name("test_ingest_lines").column("raw", "string").create()
payload = '{"a":1,"b":"world"}\n{"a":2,"b":"hello"}'

stream.ingest(payload=payload, format="lines")

```

## Examples

More sample code can be found [here](../examples/helloworld/)
