import os
import traceback
import json
import datetime
from pprint import pprint

from timeplus import Stream, Environment

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
worksapce = os.environ.get("TIMEPLUS_WORKSAPCE")

# Configure API key and address
env = Environment().address(api_address).apikey(api_key).workspace(worksapce)

try:
    # create a new stream
    stream = (
        Stream(env=env)
        .name("test_ingest")
        .column("a", "integer")
        .column("b", "string")
        # .create()
    )

    payload = """
    {"a":2,"b":"hello"}
    {"a":1,"b":"world"}
    """

    stream.ingest(payload=payload, format="streaming")
    # stream.delete()
except Exception as e:
    pprint(e)
    traceback.print_exc()
