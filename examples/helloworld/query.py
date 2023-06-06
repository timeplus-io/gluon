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
        Query(env=env).sql(query="SELECT * FROM iot")
        # .batching_pilicy(1000, 1000)
        .create()
    )
    query_id = query.metadata()["id"]
    pprint(f"created a query with id {query_id}")

    # get a query by id
    get_query = Query(env=env).get(id=query_id)
    metadata = query.metadata()
    pprint(f"get a query with id {metadata['id']}")

    # iterate query result
    limit = 10
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
