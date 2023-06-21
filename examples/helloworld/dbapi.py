import os

from timeplus.api import connect

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
workspace = os.environ.get("TIMEPLUS_WORKSPACE")

conn = connect(address=api_address, apikey=api_key, workspace=workspace)
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
