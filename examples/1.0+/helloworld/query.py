import os

from timeplus import Query, Environment

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
worksapce = os.environ.get("TIMEPLUS_WORKSAPCE")

# Configure API key and address
env = Environment().address(api_address).apikey(api_key).workspace(worksapce)

try:
    query = Query(env=env).sql(query="select * from iot").create()
    query_id = query.metadata()["id"]

    get_query = Query(env=env).get(id=query_id)
    print(query.metadata())

    limit = 10
    count = 0
    for event in query.result():
        print(event.event)
        print(event.data)
        count += 1
        if count >= limit:
            break

    query.cancel()
    query.delete()

except Exception as e:
    print(e)
