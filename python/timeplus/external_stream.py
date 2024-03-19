import swagger_client
from swagger_client.rest import ApiException

from .error import TimeplusAPIError


class ExternalStream:
    def __init__(self, env):
        """
        Initializes the External Stream object with the provided environment.

        Args:
        env: The environment in which the stream operates.
        """
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance = swagger_client.ExternalStreamsV1beta2Api(
            swagger_client.ApiClient(self._configuration)
        )
        self._metadata = None

        self._columns = None
        self._name = None
        self._description = None
        self._settings = None

    def name(self, stream_name):
        """
        Assigns a name to the stream.

        Args:
        stream_name (str): The name of the stream.

        Returns:
        ExternalStream: The current stream object.
        """
        self._name = stream_name
        return self

    def add_column(self, column_name, column_type):
        """
        Assigns a column name and type to the stream.

        Args:
        column_name (str): The name of the column.
        column_type (str): The type of the column.

        Returns:
        ExternalStream: The current stream object.
        """
        if self._columns is None:
            self._columns = []

        column = {"name": column_name, "type": column_type}
        self._columns.append(column)
        return self

    def description(self, description):
        """
        Assigns a description to the stream.

        Args:
        description (str): The description of the stream.

        Returns:
        ExternalStream: The current stream object.
        """
        self._description = description
        return self

    def add_settings(self, key, value):
        """
        Assign a setting to the stream.

        Args:
        key (str): The key of the setting.
        value (str): The value of the setting.

        Returns:
        ExternalStream: The current stream object.
        """
        if self._settings is None:
            self._settings = []

        setting = {"key": key, "value": value}
        self._settings.append(setting)
        return self

    def create(self):
        """
        Sends a request to the API to create the external stream.

        Returns:
        ExternalStream: The current external stream object.

        Raises:
        ApiException: If an error occurs during the API call.
        """

        if not self._columns:
            raise ApiException("columns is required to create external stream")

        if not self._settings:
            raise ApiException("settings is required to create external stream")

        if not self._name:
            raise ApiException("name is required to create external stream")

        body = {"columns": self._columns, "name": self._name}

        if self._description:
            body["description"] = self._description

        if self._settings:
            body["settings"] = self._settings

        try:
            self._metadata = self._api_instance.v1beta2_external_streams_post(body)
            return self
        except ApiException as e:
            raise e

    def list(self):
        """
        Fetches a list of all external streams from the API.

        Returns:
        List: A list of all external streams.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        try:
            list_response = self._api_instance.v1beta2_external_streams_get()
            return list_response
        except ApiException as e:
            raise e

    def delete(self):
        """
        Sends a request to the API to delete the stream.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        self._api_instance.v1beta2_external_streams_name_delete(self._name)

    # TODO: bug https://github.com/timeplus-io/gluon/issues/70
    def get(self):
        """
        Retrieves the metadata of the externa stream from the API.

        Returns:
        ExternalStream: The current external stream object with its metadata.

        Raises:
        TimeplusAPIError: If the external stream does not exist.
        """
        try:
            resp = self._api_instance.v1beta2_external_streams_name_get(self._name)
            self._metadata = resp
            return self
        except ApiException as e:
            raise TimeplusAPIError(f"no such stream with id {self._name} {e}")

    def metadata(self):
        """
        Retrieve the internal api object swagger_client.models.stream.Stream

        Returns:
        swagger_client.models.external_stream.ExternalStream: API object of the stream.
        """

        return self._metadata

    def exist(self):
        """
        Checks if the external stream exists.

        Returns:
        bool: True if the external stream exists, False otherwise.
        """
        streams = self.list()
        for s in streams:
            if s.name == self._name:
                return True
        return False
