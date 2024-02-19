import os
from timeplus.dbapi import connect

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = "dev.timeplus.cloud"
workspace = os.environ.get("TIMEPLUS_WORKSPACE")

conn = connect(host=api_address, password=api_key, path=workspace)
cursor = conn.execute("select * from table(car_live_data) limit 5")

next = cursor.next()
print(f"next is {next}")

row1 = cursor.fetchone()
print(f"row one is {row1}")

rows = cursor.fetchmany(3)
print("fetch multiple rows")
for row in rows:
    print(row)

# in case run following code, it will not stop due to streaming query
# for row in cursor:
#     pprint(row)

cursor = conn.execute("select 1<>2")
for row in cursor:
    print(row)
