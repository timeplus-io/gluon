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
