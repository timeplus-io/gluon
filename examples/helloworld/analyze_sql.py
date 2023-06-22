import os
import traceback
from pprint import pprint

from timeplus import Query, Environment

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
workspace = os.environ.get("TIMEPLUS_WORKSPACE")

# Configure API key and address
env = Environment().address(api_address).workspace(workspace).apikey(api_key)

try:
    analyze_result = Query(env=env).sql(query="SELECT * FROM car_live_data").analyze()
    pprint(f"query type is {analyze_result.query_type}")
    pprint(f"is streaming query? {analyze_result.is_streaming}")

except Exception as e:
    pprint(e)
    traceback.print_exc()
