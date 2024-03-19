from pprint import pprint
import swagger_client
from swagger_client.rest import ApiException
from .error import TimeplusAPIError


class Schema:
    def __init__(self, env):
        """
        Initializes the Schema object with the provided environment.

        Args:
        env: The environment in which the view operates.
        """
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance = swagger_client.SchemasV1beta2Api(
            swagger_client.ApiClient(self._configuration)
        )

        self._name = None
        self._type = "Protobuf"
        self._content = None
        self._metadata = None

    def name(self, schema_name):
        """
        Assigns a name to the schema.

        Args:
        schema_name (str): The name of the schema.

        Returns:
        Schema: The current schema object.
        """
        self._name = schema_name
        return self

    def type(self, schema_type="Protobuf"):
        """
        Defines the schema type of the schema.

        Args:
        schema_type (str): The type of the schema.

        Returns:
        Schema: The current schema object.
        """
        self._type = schema_type
        return self

    def content(self, schema_content):
        """
        Sets the content of the schema.

        Args:
        schema_content (str): The content of the schema.

        Returns:
        Schema: The current schema object.
        """
        self._content = schema_content
        return self

    def create(self):
        """
        Sends a request to the API to create the schema.

        Returns:
        Schema: The current schema object.

        Raises:
        ApiException: If an error occurs during the API call.
        """

        if not self._name:
            raise ApiException("name is required to create schema")

        if not self._type:
            raise ApiException("type is required to create schema")

        if not self._content:
            raise ApiException("content is required to create schema")

        body = {"name": self._name, "type": self._type, "content": self._content}

        try:
            self._metadata = self._api_instance.v1beta2_schemas_post(body)
            return self
        except ApiException as e:
            pprint(
                "Exception when calling SchemasV1beta2Api->v1beta2_create_schema_request: %s\n"
                % e
            )
            raise e

    def list(self):
        """
        Fetches a list of all schema from the API.

        Returns:
        List(swagger_client.models.schema_resp.SchemaResp): A list of all schemas.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        try:
            list_response = self._api_instance.v1beta2_schemas_get()
            return list_response
        except ApiException as e:
            pprint(
                "Exception when calling SchemasV1beta2Api->v1beta2_schemas_get: %s\n"
                % e
            )
            raise e

    def delete(self):
        """
        Sends a request to the API to delete the schema.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        self._api_instance.v1beta2_schemas_name_delete(self._name)

    def get(self):
        """
        Retrieves the metadata of the schema from the API.

        Returns:
        View: The current schema object with its metadata.

        Raises:
        TimeplusAPIError: If the view does not exist.
        """
        try:
            resp = self._api_instance.v1beta2_schemas_name_get(self._name)
            self._metadata = resp
            return self
        except ApiException as e:
            print(
                "Exception when calling SchemasV1beta2Api->v1beta2_schemas_name_get: %s\n"
                % e
            )
            raise TimeplusAPIError(f"no such view with id {self._name}")

    def metadata(self):
        """
        Returns the metadata of the schema.

        Returns:
        swagger_client.models..schema_resp.SchemaRespw: The api object of the schema.
        """
        return self._metadata

    def exist(self):
        """
        Checks if the schema exists.

        Returns:
        bool: True if the schema exists, False otherwise.
        """
        schemas = self.list()
        for s in schemas:
            if s.name == self._name:
                return True
        return False
