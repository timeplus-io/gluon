import os
import json

import timeplus_client
from timeplus_client.rest import ApiException
from timeplus.stream import QueryStreamV2
from pprint import pprint

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
worksapce = os.environ.get("TIMEPLUS_WORKSAPCE")


# Configure API key and address
configuration = timeplus_client.Configuration()
configuration.address(api_address)
configuration.apikey(api_key)
configuration.workspace(worksapce)

# create an instance of the API class
api_instance = timeplus_client.QueriesV1beta2Api(
    timeplus_client.ApiClient(configuration)
)

body = timeplus_client.CreateQueryRequestV1Beta2(sql="select * from iot")

try:
    # create query
    api_response = api_instance.v1beta2_queries_post(body)
    stream = QueryStreamV2(api_response)
    for event in stream.events():
        pprint(f"event : {event.event} ")
        pprint(json.loads(event.data))
except ApiException as e:
    print(
        "Exception when calling APIKeysV1beta1Api->v1beta1_auth_api_keys_get: %s\n" % e
    )
