import os
import traceback
import json
import datetime
from pprint import pprint

from timeplus import Stream, Environment

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
worksapce = os.environ.get("TIMEPLUS_WORKSPACE")

# Configure API key and address
env = Environment().address(api_address).apikey(api_key).workspace(worksapce)

try:
    # create a new stream
    stream = (
        Stream(env=env)
        .name("test_ingest")
        .column("time", "datetime64(3)")
        .column("data", "string")
        .create()
    )

    stream.ingest(["time", "data"], [[datetime.datetime.now(), "abcd"]])
    stream.delete()
except Exception as e:
    pprint(e)
    traceback.print_exc()
