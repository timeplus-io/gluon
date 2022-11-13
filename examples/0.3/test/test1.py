import os
import time

from rx import operators as ops
from timeplus import Stream, StreamColumn, Query, Env, Type


# initialize timeplus environment
api_key = "jGphdqC2PjCayDzjyck76LbNpXVSThL1vTkOVVbuoga5E0LrbO-JCK9FEJrL"
host = "duckbill.beta.timeplus.com"
env = Env().schema("https").host(host).port("444").api_key(api_key)
Env.setCurrent(env)


# query = Query().sql(
#     f"""select date_diff(second, windowEnd,now()) as sec,lpn,windowStart,windowEnd,state,avg_speed,last_speed,lat,lon
#         from table(truck_state) where lpn='沪EQ1599' and
#         windowEnd in (select max(windowEnd) from table(truck_state) where lpn='沪EQ1599')"""
# )
# query.create()

# query.get_result_stream().pipe(ops.take(5)).subscribe(
#     on_next=lambda i: print(f"get one query result {i}"),
#     on_error=lambda e: print(f"error {e}"),
#     on_completed=lambda: query.stop(),
# )

result = Query.execSQL(
    """select date_diff(second, windowEnd,now()) as sec,lpn,windowStart,windowEnd,state,avg_speed,last_speed,lat,lon
        from table(truck_state) where lpn='沪EQ1599' and
        windowEnd in (select max(windowEnd) from table(truck_state) where lpn='沪EQ1599')"""
)

print(result["data"])
