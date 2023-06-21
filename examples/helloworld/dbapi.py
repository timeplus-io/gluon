import os

from timeplus.api import connect

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = "dev.timeplus.cloud"
workspace = os.environ.get("TIMEPLUS_WORKSPACE")

conn = connect(host=api_address, password=api_key, path=workspace)
cusor = conn.execute("select * from car_live_data")

next = cusor.next()
print(f"next is {next}")

rows = cusor.fetchmany(3)
print("fetch multiple rows")
for row in rows:
    print(row)

# in case run following code, it will not stop due to streaming query
# for row in cusor:
#     pprint(row)
