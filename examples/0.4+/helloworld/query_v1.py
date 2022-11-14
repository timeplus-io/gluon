import os

import timeplus_client
from timeplus_client.rest import ApiException
from timeplus.stream import QueryStreamV1
from pprint import pprint

from rx import operators as ops

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_ADDRESS")


# Configure API key and address
configuration = timeplus_client.Configuration()
configuration.api_key["X-Api-Key"] = api_key
configuration.host = f"{api_address}/api"

# create an instance of the API class
api_instance = timeplus_client.QueriesV1beta1Api(
    timeplus_client.ApiClient(configuration)
)

body = timeplus_client.CreateQueryRequestV1Beta1(sql="select * from iot")

try:
    # create query
    api_response = api_instance.v1beta1_queries_post(body=body)
    pprint(api_response)
    stream = QueryStreamV1(configuration, api_response)
    # stream.show_result()
    pprint(stream.header())

    stream.result().pipe(ops.take(10)).subscribe(
        on_next=lambda i: pprint(f"query result {i}"),
        on_error=lambda e: stream.stop(),
        on_completed=lambda: stream.stop(),
    )

except ApiException as e:
    print(
        "Exception when calling APIKeysV1beta1Api->v1beta1_auth_api_keys_get: %s\n" % e
    )
