import os
from timeplus import Query, Env

# initialize timeplus environment
api_key = os.environ.get("TIMEPLUS_API_KEY")
env = Env().api_key(api_key)

for query in Query.list():
    query.cancel()
    query.delete()
