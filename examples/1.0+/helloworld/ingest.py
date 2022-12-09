import os

import timeplus_client
from timeplus_client.rest import ApiException
from timeplus.stream import QueryStreamV1
from pprint import pprint


api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
worksapce = os.environ.get("TIMEPLUS_WORKSAPCE")


# Configure API key and address
configuration = timeplus_client.Configuration()
configuration.address(api_address)
configuration.apikey(api_key)
configuration.workspace(worksapce)

api_instance = timeplus_client.StreamsV1beta1Api(
    timeplus_client.ApiClient(configuration)
)

body = timeplus_client.IngestData(["a"], [[1], [2], [3]])
name = "test"  # str | stream name

try:
    # ingest data.
    api_instance.v1beta1_streams_name_ingest_post(body, name)
except ApiException as e:
    print(
        "Exception when calling StreamsV1beta1Api->v1beta1_streams_name_ingest_post: %s\n"
        % e
    )
