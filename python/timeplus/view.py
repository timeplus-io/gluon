from pprint import pprint
import swagger_client
from swagger_client.rest import ApiException
from .error import TimeplusAPIError


class View:
    def __init__(self, env):
        """
        Initializes the View object with the provided environment.

        Args:
        env: The environment in which the view operates.
        """
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance = swagger_client.ViewsV1beta2Api(
            swagger_client.ApiClient(self._configuration)
        )

        self._name = None
        self._query = None
        self._metadata = None

        self._materialized = None
        self._description = None
        self._target_stream = None

    def name(self, view_name):
        """
        Assigns a name to the view.

        Args:
        view_name (str): The name of the view.

        Returns:
        View: The current view object.
        """
        self._name = view_name
        return self

    def query(self, view_query):
        """
        Defines the SQL query of the view.

        Args:
        view_query (str): The SQL query of the view.

        Returns:
        View: The current view object.
        """
        self._query = view_query
        return self

    def materialized(self, view_materialized):
        """
        Sets whether the view is materialized or not.

        Args:
        view_materialized (bool): If True, the view is materialized.

        Returns:
        View: The current view object.
        """
        self._materialized = view_materialized
        return self

    def target_stream(self, view_target_stream):
        """
        Assigns a target stream to the view.

        Args:
        view_target_stream (str): The name of the target stream.

        Returns:
        View: The current view object.
        """
        self._target_stream = view_target_stream
        return self

    def description(self, view_description):
        """
        Sets the description of the view.

        Args:
        view_description (str): The description of the view.

        Returns:
        View: The current view object.
        """
        self._description = view_description
        return self

    def create(self):
        """
        Sends a request to the API to create the view.

        Returns:
        View: The current view object.

        Raises:
        ApiException: If an error occurs during the API call.
        """

        if not self._query:
            raise ApiException("query sql is required to create view")

        if not self._name:
            raise ApiException("name is required to create view")

        body = {"name": self._name, "query": self._query}

        if self._materialized:
            body["materialized"] = self._materialized

        if self._description:
            body["description"] = self._description

        if self._target_stream:
            body["target_stream"] = self._target_stream

        try:
            self._metadata = self._api_instance.v1beta2_views_post(body)
            return self
        except ApiException as e:
            pprint(
                "Exception when calling ViewsV1beta2Api->v1beta2_views_post: %s\n" % e
            )
            raise e

    def list(self):
        """
        Fetches a list of all views from the API.

        Returns:
        List(swagger_client.models.view.View): A list of all views.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        try:
            list_response = self._api_instance.v1beta2_views_get()
            return list_response
        except ApiException as e:
            pprint(
                "Exception when calling ViewsV1beta2Api->v1beta2_views_get: %s\n" % e
            )
            raise e

    def delete(self):
        """
        Sends a request to the API to delete the view.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        self._api_instance.v1beta2_views_name_delete(self._name)

    # bug : refer tom https://github.com/timeplus-io/gluon/issues/70
    def get(self):
        """
        Retrieves the metadata of the view from the API.

        Returns:
        View: The current view object with its metadata.

        Raises:
        TimeplusAPIError: If the view does not exist.
        """
        try:
            resp = self._api_instance.v1beta2_views_name_get(self._name)
            self._metadata = resp
            return self
        except ApiException as e:
            print(
                "Exception when calling ViewsV1beta2Api->v1beta2_views_name_get: %s\n"
                % e
            )
            raise TimeplusAPIError(f"no such view with id {self._name}")

    def metadata(self):
        """
        Returns the metadata of the view.

        Returns:
        swagger_client.models.view.View: The api object of the view.
        """
        return self._metadata

    def exist(self):
        """
        Checks if the view exists.

        Returns:
        bool: True if the view exists, False otherwise.
        """
        views = self.list()
        for s in views:
            if s.name == self._name:
                return True
        return False
