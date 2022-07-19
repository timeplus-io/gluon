## Timeplus API Python SDK

Timeplus Python SDK

to install the sdk, run `pip install timeplus`

```python
import os

from rx import operators as ops
from timeplus import Stream, StreamColumn, Query, Env, Type

# initialize timeplus environment
api_key = os.environ.get("TIMEPLUS_API_KEY")
env = (
    Env().schema("https").host("hostname").port("443").api_key(api_key)
)
Env.setCurrent(env)

# create a stream
s = (
    Stream()
    .name("stream_name")
    .column(StreamColumn().name("field_name_a").type(Type.String))
    .column(StreamColumn().name("field_name_b").type(Type.Float))
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