import json
import sseclient

from pprint import pprint
from websocket import create_connection, WebSocketConnectionClosedException

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
        self.stopped = False
        self._create_response = None
        self._id = None

    def sql(self, query):
        self._sql = query
        return self

    def create(self):
        body = swagger_client.CreateQueryRequestV1Beta2(sql=self._sql)
        try:
            self._create_response = self._api_instance_v2.v1beta2_queries_post(body)
            # TODO: how to handle the id and the first result here
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
        except Exception as e:
            pprint(e)

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
        except Exception as e:
            pprint(e)

    def get(self, id):
        self._id = id
        # send get request here
        try:
            self._get_response = self._api_instance_v1.v1beta1_queries_id_get(
                id=self._id
            )
            self._metadata = json.loads(self._get_response)
            return self
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta1Api->v1beta1_queries_id_get: %s\n"
                % e
            )
        except Exception as e:
            pprint(e)
