from pprint import pprint
import swagger_client
from swagger_client.rest import ApiException

from .error import TimeplusAPIError


class Stream:
    def __init__(self, env):
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance = swagger_client.StreamsV1beta1Api(
            swagger_client.ApiClient(self._configuration)
        )
        self._id = None
        self._body = None
        self._columns = None

    def name(self, stream_name):
        self._name = stream_name
        return self

    def column(self, column_name, column_type):
        if self._columns is None:
            self._columns = []

        column = {"name": column_name, "type": column_type}
        self._columns.append(column)
        return self

    def create(self):
        body = {"columns": self._columns, "name": self._name}
        try:
            self._metadata = self._api_instance.v1beta1_streams_post(body)
            return self
        except ApiException as e:
            pprint(
                "Exception when calling StreamsV1beta1Api->v1beta1_streams_post: %s\n"
                % e
            )
            raise e

    def list(self):
        try:
            list_response = self._api_instance.v1beta1_streams_get()
            return list_response
        except ApiException as e:
            pprint(
                "Exception when calling StreamsV1beta1Api->v1beta1_streams_get: %s\n"
                % e
            )
            raise e

    def delete(self):
        self._api_instance.v1beta1_streams_name_delete(self._name)

    def get(self):
        streams = self.list()
        for s in streams:
            if s.name == self._name:
                self._metadata = s
                return self
        raise TimeplusAPIError(f"not such stream {self._name}")

    def metadata(self):
        return self._metadata

    def ingest(self, colums=None, rows=None, payload=None, format="compact"):
        if format == "compact":
            body = swagger_client.IngestData(colums, rows)
            try:
                self._api_instance.v1beta1_streams_name_ingest_post(body, self._name)
            except ApiException as e:
                pprint(
                    "Exception when calling StreamsV1beta1Api->v1beta1_streams_name_ingest_post: %s\n"
                    % e
                )
                raise e
        else:
            try:
                self._api_instance.v1beta1_streams_name_ingest_post(
                    body=payload, name=self._name, format=format
                )
            except ApiException as e:
                pprint(
                    "Exception when calling StreamsV1beta1Api->v1beta1_streams_name_ingest_post: %s\n"
                    % e
                )
                raise e

    def exist(self):
        streams = self.list()
        for s in streams:
            if s.name == self._name:
                return True
        return False
