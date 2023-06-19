# timeplus-client

Welcome to the Timeplus HTTP REST API specification.

# query

```python
import json
import sseclient

from pprint import pprint

import swagger_client
from swagger_client.rest import ApiException


class Query:
    def __init__(self, env):
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance = swagger_client.QueriesV1beta2Api(
            swagger_client.ApiClient(self._configuration)
        )
        self._create_response = None
        self._id = None
        self._batching_policy = None

    def sql(self, query):
        self._sql = query
        return self

    # refer to https://docs.timeplus.com/rest.html#tag/Queries-v1beta2/paths/~1v1beta2~1queries/post
    # count : The max result count per batch
    # time_ms : The max interval per batch in milliseconds
    def batching_policy(self, count, time_ms):
        self._batching_policy = swagger_client.models.BatchingPolicy(
            count=count, time_ms=time_ms
        )
        return self

    def create(self):
        body = swagger_client.CreateQueryRequestV1Beta2(
            sql=self._sql, batching_policy=self._batching_policy
        )
        try:
            # as to support sse, the reponse is urllib3.response.HTTPResponse
            # instead of swagger_client.models.query.Query
            self._create_response = self._api_instance.v1beta2_queries_post(body)
            _sse_client = sseclient.SSEClient(self._create_response)
            self._events = _sse_client.events()
            self._query = next(self._events)
            self._metadata = json.loads(self._query.data)
            self._id = self._metadata["id"]
            return self
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta2Api->v1beta2_queries_post: %s\n"
                % e
            )
            raise e

    def metadata(self):
        return self._metadata

    def id(self):
        return self._id

    def header(self):
        return self._metadata["result"]["header"]

    def result(self):
        return self._events

    def delete(self):
        self._api_instance.v1beta2_queries_id_delete(self._id)

    def cancel(self):
        try:
            self._cancel_response = self._api_instance.v1beta2_queries_id_cancel_post(
                id=self._id
            )
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta2Api->v1beta2_queries_id_cancel_post: %s\n"
                % e
            )
            raise e

    def get(self, id):
        self._id = id
        try:
            self._get_response = self._api_instance.v1beta2_queries_id_get(id=self._id)
            self._metadata = self._get_response
            return self
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta2Api->v1beta2_queries_id_get: %s\n"
                % e
            )
            raise e

    def list(self):
        try:
            list_response = self._api_instance.v1beta2_queries_get()
            return list_response
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta2Api->v1beta2_queries_id_get: %s\n"
                % e
            )
            raise e
```

# stream

```python
import os
import traceback
import json
from pprint import pprint

from timeplus import Stream, Environment

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
worksapce = os.environ.get("TIMEPLUS_WORKSAPCE")

# Configure API key and address
env = Environment().address(api_address).apikey(api_key).workspace(worksapce)

try:
    # list all streams
    stream_list = Stream(env=env).list()
    pprint(f"there are {len(stream_list)} streams ")

    # create a new stream
    stream = (
        Stream(env=env)
        .name("test")
        .column("time", "datetime64(3)")
        .column("data", "string")
        .create()
    )

    stream_list = Stream(env=env).list()
    pprint(f"there are {len(stream_list)} streams after create")
    pprint(f"created stream is {stream.metadata()}; type is {type(stream.metadata())}")

    a_stream = Stream(env=env).name("test").get()
    pprint(f"get stream is {a_stream.metadata()} ; type is {type(a_stream.metadata())}")

    stream.delete()
    stream_list = Stream(env=env).list()
    pprint(f"there are {len(stream_list)} streams after delete")
except Exception as e:
    pprint(e)
    traceback.print_exc()

```

# ingest

default ingest

```python
stream = (
        Stream(env=env)
        .name("test_ingest")
        .column("time", "datetime64(3)")
        .column("data", "string")
        .create()
    )

stream.ingest(["time", "data"], [[datetime.datetime.now(), "abcd"]])

```

ingest json streams

```python
stream = (
        Stream(env=env)
        .name("test_ingest")
        .column("a", "integer")
        .column("b", "string")
        .create()
    )

payload = """
{"a":2,"b":"hello"}
{"a":1,"b":"world"}
"""

stream.ingest(payload=payload, format="streaming")

```

ingest one raw event with multiple lines

```python
stream = Stream(env=env).name("test_ingest_raw").column("raw", "string").create()

payload = """
first line
second line
"""

stream.ingest(payload=payload, format="raw")

```

ingest multiple lines

```python
stream = Stream(env=env).name("test_ingest_lines").column("raw", "string").create()
payload = '{"a":1,"b":"world"}\n{"a":2,"b":"hello"}'

stream.ingest(payload=payload, format="lines")

```
