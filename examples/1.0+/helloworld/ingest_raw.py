import os
import traceback
from pprint import pprint

from timeplus import Stream, Environment

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_ADDRESS")

# Configure API key and address
env = Environment().address(api_address).apikey(api_key)

try:
    # create a new stream
    stream = Stream(env=env).name("test_ingest_raw").column("raw", "string").create()

    payload = """
    {"a":1,"b":"world"}
    {"a":2,"b":"hello"}
    """

    stream.ingest(payload=payload, format="raw")
    # stream.delete()
except Exception as e:
    pprint(e)
    traceback.print_exc()
