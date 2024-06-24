from pprint import pprint
import swagger_client
from swagger_client.rest import ApiException

from .error import TimeplusAPIError


class Stream:
    def __init__(self, env):
        """
        Initializes the Stream object with the provided environment.

        Args:
        env: The environment in which the stream operates.
        """
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance = swagger_client.StreamsV1beta2Api(
            swagger_client.ApiClient(self._configuration)
        )
        self._body = None
        self._columns = None

        self._event_time_timezone = None
        self._event_time_cloumn = None
        self._logstore_retention_bytes = None
        self._logstore_retention_ms = None
        self._ttl_expression = None
        self._description = None
        self._mode = "append"
        self._primary_key = None
        self._replication_factor = None
        self._shards = None

    def name(self, stream_name):
        """
        Assigns a name to the stream.

        Args:
        stream_name (str): The name of the stream.

        Returns:
        Stream: The current stream object.
        """
        self._name = stream_name
        return self

    def column(self, column_name, column_type):
        """
        Assigns a column name and type to the stream.

        Args:
        column_name (str): The name of the column.
        column_type (str): The type of the column.

        Returns:
        Stream: The current stream object.
        """
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

    def replication_factor(self, replication_factor):
        self._replication_factor = replication_factor
        return self

    def shards(self, shards):
        self._shards = shards
        return self

    def create(self):
        """
        Sends a request to the API to create the stream.

        Returns:
        Stream: The current stream object.

        Raises:
        ApiException: If an error occurs during the API call.
        """

        if not self._columns or not self._name:
            raise ApiException("columns or name is required to create stream")

        body = {"columns": self._columns, "name": self._name}

        body["event_time_column"] = (
            self._event_time_cloumn if self._event_time_cloumn else None
        )
        body["event_time_timezone"] = (
            self._event_time_timezone if self._event_time_timezone else None
        )
        body["logstore_retention_bytes"] = (
            self._logstore_retention_bytes if self._logstore_retention_bytes else None
        )
        body["logstore_retention_ms"] = (
            self._logstore_retention_ms if self._logstore_retention_ms else None
        )
        body["ttl_expression"] = self._ttl_expression if self._ttl_expression else None
        body["description"] = self._description if self._description else None
        body["mode"] = self._mode if self._mode else None
        body["primary_key"] = self._primary_key if self._primary_key else None
        body["replication_factor"] = (
            self._replication_factor if self._replication_factor else None
        )
        body["shards"] = self._shards if self._shards else None

        try:
            self._metadata = self._api_instance.v1beta2_streams_post(body)
            return self
        except ApiException as e:
            pprint(
                "Exception when calling StreamsV1beta2Api->v1beta2_streams_post: %s\n"
                % e
            )
            raise e

    def list(self):
        """
        Fetches a list of all streams from the API.

        Returns:
        List: A list of all streams.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        try:
            list_response = self._api_instance.v1beta2_streams_get()
            return list_response
        except ApiException as e:
            pprint(
                "Exception when calling StreamsV1beta2Api->v1beta2_streams_get: %s\n"
                % e
            )
            raise e

    def delete(self):
        """
        Sends a request to the API to delete the stream.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        self._api_instance.v1beta2_streams_name_delete(self._name)

    # TODO: bug https://github.com/timeplus-io/gluon/issues/70
    def get(self):
        """
        Retrieves the metadata of the stream from the API.

        Returns:
        Stream: The current stream object with its metadata.

        Raises:
        TimeplusAPIError: If the stream does not exist.
        """
        try:
            resp = self._api_instance.v1beta2_streams_name_get(self._name)
            self._metadata = resp
            return self
        except ApiException as e:
            pprint(
                "Exception when calling StreamsV1beta2Api->v1beta2_streams_name_get: %s\n"
                % e
            )
            raise TimeplusAPIError(f"no such stream with id {self._name}")

    def metadata(self):
        """
        Retrieve the internal api object swagger_client.models.stream.Stream

        Returns:
        swagger_client.models.stream.Stream: API object of the stream.
        """

        return self._metadata

    def ingest(self, colums=None, rows=None, payload=None, format="compact"):
        """
        Sends a request to the API to ingest data into the stream.

        Args:
        columns (list, optional): The columns in the data.
        rows (list, optional): The rows in the data.
        payload (any, optional): The payload to be ingested.
        format (str, optional): The format of the data. Defaults to "compact".

        Raises:
        ApiException: If an error occurs during the API call.
        """
        if format == "compact":
            body = swagger_client.IngestData(colums, rows)
            try:
                self._api_instance.v1beta2_streams_name_ingest_post(body, self._name)
            except ApiException as e:
                pprint(
                    "Exception when calling StreamsV1beta2Api->v1beta2_streams_name_ingest_post: %s\n"
                    % e
                )
                raise e
        else:
            try:
                self._api_instance.v1beta2_streams_name_ingest_post(
                    body=payload, name=self._name, format=format
                )
            except ApiException as e:
                pprint(
                    "Exception when calling StreamsV1beta2Api->v1beta2_streams_name_ingest_post: %s\n"
                    % e
                )
                raise e

    def exist(self):
        """
        Checks if the stream exists.

        Returns:
        bool: True if the stream exists, False otherwise.
        """
        streams = self.list()
        for s in streams:
            if s.name == self._name:
                return True
        return False
