import os
import time

from rx import operators as ops
from timeplus import Stream, StreamColumn, Query, Env, Type

# initialize timeplus environment
api_key = os.environ.get("TIMEPLUS_API_KEY")
host = os.environ.get("TIMEPLUS_HOST")
env = Env().schema("https").host(host).port("443").api_key(api_key)
Env.setCurrent(env)

stream_name = "dummy"
# create a stream
s = (
    Stream()
    .name(stream_name)
    .column(StreamColumn().name("field_name_a").type(Type.String))
    .column(StreamColumn().name("field_name_b").type(Type.Float))
)

try:
    s.delete()
except Exception as e:
    env.logger().debug(f"failed to delete stream {e}")


s.create()

# insert data into stream
s.insert(
    [
        ["hello", 100.1],
        ["timeplus", 20.2],
    ]
)

# wait for the event to be ingested
time.sleep(3)

result = Query.execSQL(f"select * from table({stream_name})")
env.logger().debug(f"query result is {result}")

# run query on existing stream
query = Query().sql(f"select * from table({stream_name})")
query.create()

# query.show_query_result()

# query.get_result_stream().pipe(ops.take(2)).subscribe(
#     on_next=lambda i: env.logger().info(f"get one query result {i}"),
#     on_error=lambda e: env.logger().error(f"error {e}"),
#     on_completed=lambda: query.stop(),
# )

# delete stream
s.delete()
