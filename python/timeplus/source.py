import swagger_client
from swagger_client.rest import ApiException
from .error import TimeplusAPIError


class Source:
    def __init__(self, env):
        """
        Initializes the Source object with the provided environment.

        Args:
        env: The environment in which the source operates.
        """
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance = swagger_client.SourcesV1beta2Api(
            swagger_client.ApiClient(self._configuration)
        )

        self._name = None
        self._type = None
        self._description = None
        self._stream = None
        self._properties = None
        self._metadata = {}

    def name(self, source_name):
        """
        Assigns a name to the source.

        Args:
        source_name (str): The name of the source.

        Returns:
        Source: The current source object.
        """
        self._name = source_name
        return self

    def type(self, source_type):
        """
        Defines the type of the source.

        Args:
        source_type (str): The type of the source.

        Returns:
        Source: The current source object.
        """
        self._type = source_type
        return self

    def description(self, source_description):
        """
        Sets the description of the source.

        Args:
        source_description (str): The description of the source.

        Returns:
        Source: The current source object.
        """
        self._description = source_description
        return self

    def stream(self, source_stream):
        """
        Sets the target stream for the source.

        Args:
        source_stream (str): The name of the target stream.

        Returns:
        Source: The current source object.
        """
        self._stream = source_stream
        return self

    def properties(self, source_properties):
        """
        Sets additional properties required to read the data from source.

        Args:
        source_properties (dict): Additional properties.

        Returns:
        Source: The current source object.
        """
        self._properties = source_properties
        return self

    def id(self, *args):
        if len(args) == 0:  # get id
            if "id" not in self._metadata:
                raise ApiException("id is not provided")
            return self._metadata["id"]
        elif len(args) == 1:  # set id
            new_value = args[0]
            self._metadata["id"] = new_value
            return self
        else:
            raise ApiException("id() accepts at most 1 argument")

        return self._metadata["id"]

    def create(self):
        """
        Sends a request to the API to create the source.

        Returns:
        Source: The current source object.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        body = {}

        if self._name:
            body["name"] = self._name
        else:
            raise ApiException("name is required to create source")

        if self._type:
            body["type"] = self._type
        else:
            raise ApiException("type is required to create source")

        if self._stream:
            body["stream"] = self._stream
        else:
            raise ApiException("stream is required to create source")

        if self._properties:
            body["properties"] = self._properties
        else:
            raise ApiException("properties is required to create source")

        if self._description:
            body["description"] = self._description

        try:
            resp = self._api_instance.v1beta2_sources_post(body)
            self._metadata = resp.to_dict()  # return dict of the response object
            return self
        except ApiException as e:
            print(
                "Exception when calling SourcesV1beta2Api->v1beta2_sources_post: %s\n"
                % e
            )
            raise e

    def list(self):
        """
        Fetches a list of all sources from the API.

        Returns:
        List(swagger_client.models.source.Source): A list of all sources.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        try:
            list_response = self._api_instance.v1beta2_sources_get()
            return list_response
        except ApiException as e:
            print(
                "Exception when calling SourcesV1beta2Api->v1beta2_sources_get: %s\n"
                % e
            )
            raise e

    def delete(self):
        """
        Sends a request to the API to delete the source.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        self._api_instance.v1beta2_sources_id_delete(self.id())

    def get(self):
        """
        Retrieves the metadata of the source from the API.

        Returns:
        Source: The current source object with its metadata.

        Raises:
        TimeplusAPIError: If the source does not exist.
        """
        try:
            resp = self._api_instance.v1beta2_sources_id_get(self.id())
            self._metadata = resp.to_dict()
            return self
        except ApiException as e:
            print(
                "Exception when calling SourcesV1beta2Api->v1beta2_sources_id_get: %s\n"
                % e
            )
            raise TimeplusAPIError(f"no such source with id {self.id()}")

    def metadata(self):
        """
        Returns the metadata of the source.

        Returns:
        swagger_client.models.source.Source: The metadata of the source.
        """
        return self._metadata

    def update(self, body):
        """
        Update the specific source with the given ID.

        Args:
        body (dict): A dictionary containing the parameters to update.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        self._api_instance.v1beta2_sources_id_put(self.id(), body)

    def exist(self):
        """
        Checks if the source exists.

        Returns:
        bool: True if the source exists, False otherwise.
        """
        try:
            self._api_instance.v1beta2_sources_id_get(self.id())
            return True
        except ApiException:
            return False

    def start(self):
        """
        start the source

        Returns:
        Source: The current source object.
        """
        try:
            self._api_instance.v1beta2_sources_id_start_post(self.id())
            return self
        except ApiException:
            return False

    def stop(self):
        """
        stop the source

        Returns:
        Source: The current source object.
        """
        try:
            self._api_instance.v1beta2_sources_id_stop_post(self.id())
            return self
        except ApiException:
            return False
