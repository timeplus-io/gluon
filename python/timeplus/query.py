import json
import sseclient

from pprint import pprint

import swagger_client
from swagger_client.rest import ApiException


class Query:
    def __init__(self, env):
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance_v1 = swagger_client.QueriesV1beta1Api(
            swagger_client.ApiClient(self._configuration)
        )
        self._api_instance_v2 = swagger_client.QueriesV1beta2Api(
            swagger_client.ApiClient(self._configuration)
        )
        self._create_response = None
        self._id = None
        self._batching_pilicy = None

    def sql(self, query):
        self._sql = query
        return self

    def batching_pilicy(self, count, time_ms):
        self._batching_pilicy = swagger_client.models.BatchingPolicy(
            count=count, time_ms=time_ms
        )
        return self

    def create(self):
        body = swagger_client.CreateQueryRequestV1Beta2(
            sql=self._sql, batching_policy=self._batching_pilicy
        )
        try:
            # as to support sse, the reponse is urllib3.response.HTTPResponse
            # instead of swagger_client.models.query.Query
            self._create_response = self._api_instance_v2.v1beta2_queries_post(body)
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

    def result(self):
        return self._events

    def delete(self):
        self._api_instance_v1.v1beta1_queries_id_delete(self._id)

    def cancel(self):
        try:
            self._cancel_response = (
                self._api_instance_v1.v1beta1_queries_id_cancel_post(id=self._id)
            )
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta1Api->v1beta1_queries_id_cancel_post: %s\n"
                % e
            )
            raise e

    def get(self, id):
        self._id = id
        try:
            self._get_response = self._api_instance_v1.v1beta1_queries_id_get(
                id=self._id
            )
            self._metadata = self._get_response
            return self
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta1Api->v1beta1_queries_id_get: %s\n"
                % e
            )
            raise e

    def list(self):
        try:
            list_response = self._api_instance_v1.v1beta1_queries_get()
            return list_response
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta1Api->v1beta1_queries_id_get: %s\n"
                % e
            )
            raise e
