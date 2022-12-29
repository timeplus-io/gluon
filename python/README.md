# timeplus-client

Welcome to the Timeplus HTTP REST API specification.

# query

```python
import os
import traceback
import json
from pprint import pprint

from timeplus import Query, Environment

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
worksapce = os.environ.get("TIMEPLUS_WORKSAPCE")

# Configure API key and address
env = Environment().address(api_address).apikey(api_key).workspace(worksapce)

try:
    # list all qeuries
    query_list = Query(env=env).list()
    pprint(f"there are {len(query_list)} queries ")

    # create a new query
    query = Query(env=env).sql(query="SELECT * FROM iot").create()
    query_id = query.metadata()["id"]
    pprint(f"created a query with id {query_id}")

    # get a query by id
    get_query = Query(env=env).get(id=query_id)
    metadata = query.metadata()
    pprint(f"get a query with id {metadata['id']}")

    # iterate query result
    limit = 3
    count = 0
    for event in query.result():
        print(event.event)
        print(json.loads(event.data))
        count += 1
        if count >= limit:
            break

    query.cancel()
    query.delete()

except Exception as e:
    pprint(e)
    traceback.print_exc()
```

# stream

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

# ingest

default ingest

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

ingest json streams

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

ingest one raw event with multiple lines

```python
stream = Stream(env=env).name("test_ingest_raw").column("raw", "string").create()

payload = """
first line
second line
"""

stream.ingest(payload=payload, format="raw")

```

ingest multiple lines

```python
stream = Stream(env=env).name("test_ingest_lines").column("raw", "string").create()
payload = '{"a":1,"b":"world"}\n{"a":2,"b":"hello"}'

stream.ingest(payload=payload, format="lines")

```
