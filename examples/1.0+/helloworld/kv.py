import os
import traceback
from pprint import pprint

from timeplus import Stream, Environment

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_ADDRESS")

# Configure API key and address
env = Environment().address(api_address).apikey(api_key)
name = "testkv"

try:
    # list all streams
    stream_list = Stream(env=env).list()
    pprint(f"there are {len(stream_list)} streams ")

    # create a new stream
    stream = (
        Stream(env=env)
        .name(name)
        .column("id", "string")
        .column("data", "string")
        .mode("versioned_kv")
        .primary_key("id")
        .create()
    )

    stream_list = Stream(env=env).list()
    pprint(f"there are {len(stream_list)} streams after create")
    pprint(f"created stream is {stream.metadata()}; type is {type(stream.metadata())}")

    a_stream = Stream(env=env).name(name).get()
    pprint(f"get stream is {a_stream.metadata()} ; type is {type(a_stream.metadata())}")

    # stream.delete()
    stream_list = Stream(env=env).list()
    pprint(f"there are {len(stream_list)} streams after delete")
except Exception as e:
    pprint(e)
    traceback.print_exc()
