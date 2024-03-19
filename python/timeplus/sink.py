import swagger_client
from swagger_client.rest import ApiException
from .error import TimeplusAPIError


class Sink:
    def __init__(self, env):
        """
        Initializes the Sink object with the provided environment.

        Args:
        env: The environment in which the sink operates.
        """
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance = swagger_client.SinksV1beta2Api(
            swagger_client.ApiClient(self._configuration)
        )

        self._name = None
        self._type = None
        self._description = None
        self._query = None
        self._properties = None
        self._metadata = {}

    def name(self, sink_name):
        """
        Assigns a name to the sink.

        Args:
        sink_name (str): The name of the sink.

        Returns:
        Sink: The current sink object.
        """
        self._name = sink_name
        return self

    def type(self, sink_type):
        """
        Defines the type of the sink.

        Args:
        sink_type (str): The type of the sink Available types:
        [slack, http, kafka, redpanda, confluent_cloud, pulsar, timeplus].

        Returns:
        Sink: The current sink object.
        """
        self._type = sink_type
        return self

    def description(self, sink_description):
        """
        Sets the description of the sink.

        Args:
        sink_description (str): The description of the sink.

        Returns:
        Sink: The current sink object.
        """
        self._description = sink_description
        return self

    def query(self, query):
        """
        Sets the query for the sink.

        Args:
        query (str): The query of the sink.

        Returns:
        Sink: The current sink object.
        """
        self._query = query
        return self

    def properties(self, sink_properties):
        """
        Sets additional properties required for sink.

        Args:
        sink_properties (dict): Additional properties.

        Returns:
        Sink: The current sink object.
        """
        self._properties = sink_properties
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
        Sends a request to the API to create the sink.

        Returns:
        Sink: The current sink object.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        body = {}

        if self._name:
            body["name"] = self._name
        else:
            raise ApiException("name is required to create sink")

        if self._type:
            body["type"] = self._type
        else:
            raise ApiException("type is required to create sink")

        if self._query:
            body["query"] = self._query
        else:
            raise ApiException("query is required to create sink")

        if self._properties:
            body["properties"] = self._properties
        else:
            raise ApiException("properties is required to create sink")

        if self._description:
            body["description"] = self._description

        try:
            resp = self._api_instance.v1beta2_sinks_post(body)
            self._metadata = resp.to_dict()  # return dict of the response object
            return self
        except ApiException as e:
            print(
                "Exception when calling SinksV1beta2Api->v1beta2_sinks_post: %s\n" % e
            )
            raise e

    def list(self):
        """
        Fetches a list of all sink from the API.

        Returns:
        List(swagger_client.models.sink.Sink): A list of all sinks.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        try:
            list_response = self._api_instance.v1beta2_sinks_get()
            return list_response
        except ApiException as e:
            print("Exception when calling SinksV1beta2Api->v1beta2_sinks_get: %s\n" % e)
            raise e

    def delete(self):
        """
        Sends a request to the API to delete the sink.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        self._api_instance.v1beta2_sinks_id_delete(self.id())

    def get(self):
        """
        Retrieves the metadata of the sink from the API.

        Returns:
        Sink: The current sink object with its metadata.

        Raises:
        TimeplusAPIError: If the sink does not exist.
        """
        try:
            resp = self._api_instance.v1beta2_sinks_id_get(self.id())
            self._metadata = resp.to_dict()
            return self
        except ApiException as e:
            print(
                "Exception when calling SinksV1beta2Api->v1beta2_sinks_id_get: %s\n" % e
            )
            raise TimeplusAPIError(f"no such sink with id {self.id()}")

    def metadata(self):
        """
        Returns the metadata of the sink.

        Returns:
        swagger_client.models.stream.Sink: The metadata of the sink.
        """
        return self._metadata

    def update(self):
        """
        Update the specific sink with the given ID.

        Args:
        body (dict): A dictionary containing the parameters to update.

        Raises:
        ApiException: If an error occurs during the API call.
        """

        body = {}

        if self._name:
            body["name"] = self._name
        else:
            raise ApiException("name is required to update sink")

        if self._type:
            body["type"] = self._type
        else:
            raise ApiException("type is required to update sink")

        if self._query:
            body["query"] = self._query

        if self._properties:
            body["properties"] = self._properties

        if self._description:
            body["description"] = self._description

        self._api_instance.v1beta2_sinks_id_put(self.id(), body)

    def exist(self):
        """
        Checks if the sink exists.

        Returns:
        bool: True if the sink exists, False otherwise.
        """
        try:
            self._api_instance.v1beta2_sinks_id_get(self.id())
            return True
        except ApiException:
            return False

    def start(self):
        """
        start the sink

        Returns:
        Sink: The current sink object.
        """

        # this should not use internal API
        try:
            self._api_instance.v1beta2_sinks_id_start_post(self.id())
            return self
        except ApiException:
            return False

    def stop(self):
        """
        stop the sink

        Returns:
        Sink: The current sink object.
        """
        try:
            self._api_instance.v1beta2_sinks_id_stop_post(self.id())
            return self
        except ApiException:
            return False
