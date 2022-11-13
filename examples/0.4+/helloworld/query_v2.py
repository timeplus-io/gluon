import os
import sseclient
import json

import timeplus_client
from timeplus_client.rest import ApiException
from pprint import pprint

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_ADDRESS")


# Configure API key and address
configuration = timeplus_client.Configuration()
configuration.api_key["X-Api-Key"] = api_key
configuration.host = f"{api_address}/api"

# create an instance of the API class
api_instance = timeplus_client.QueriesV1beta2Api(
    timeplus_client.ApiClient(configuration)
)

body = timeplus_client.CreateQueryRequestV1Beta2(sql="select 1")

try:
    # create query
    api_response = api_instance.v1beta2_queries_post(body)
    client = sseclient.SSEClient(api_response)
    for event in client.events():
        pprint(json.loads(event.data))
except ApiException as e:
    print(
        "Exception when calling APIKeysV1beta1Api->v1beta1_auth_api_keys_get: %s\n" % e
    )
