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

        self._event_time_timezone = None
        self._event_time_cloumn = None
        self._logstore_retention_bytes = None
        self._logstore_retention_ms = None
        self._ttl_expression = None
        self._description = None
        self._mode = None
        self._primary_key = None

    def name(self, stream_name):
        self._name = stream_name
        return self

    def column(self, column_name, column_type):
        if self._columns is None:
            self._columns = []

        column = {"name": column_name, "type": column_type}
        self._columns.append(column)
        return self

    def event_time_timezone(self, timezone):
        self._event_time_timezone = timezone
        return self

    def event_time_cloumn(self, column):
        self._event_time_cloumn = column
        return self

    def logstore_retention_bytes(self, retention):
        self._logstore_retention_bytes = retention
        return self

    def logstore_retention_ms(self, retention):
        self._logstore_retention_ms = retention
        return self

    def ttl_expression(self, ttl):
        self._ttl_expression = ttl
        return self

    def description(self, description):
        self._description = description
        return self

    def mode(self, mode):
        self._mode = mode
        return self

    def primary_key(self, primary_key):
        self._primary_key = primary_key
        return self

    def create(self):
        body = {"columns": self._columns, "name": self._name}

        if self._event_time_cloumn:
            body["event_time_column"] = self._event_time_cloumn

        if self._event_time_timezone:
            body["event_time_timezone"] = self._event_time_timezone

        if self._logstore_retention_bytes:
            body["logstore_retention_bytes"] = self._logstore_retention_bytes

        if self._logstore_retention_ms:
            body["logstore_retention_ms"] = self._logstore_retention_ms

        if self._ttl_expression:
            body["ttl_expression"] = self._ttl_expression

        if self._description:
            body["description"] = self._description

        if self._mode:
            body["mode"] = self._mode

        if self._primary_key:
            body["primary_key"] = self._primary_key

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
