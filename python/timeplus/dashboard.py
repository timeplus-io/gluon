from pprint import pprint
import swagger_client
from swagger_client.rest import ApiException


class Dashboard:
    def __init__(self, env):
        """
        Initializes the Dashboard object with the provided environment.

        Args:
        env: The environment in which the view operates.
        """
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance = swagger_client.DashboardsV1beta2Api(
            swagger_client.ApiClient(self._configuration)
        )

    def list(self):
        """
        Fetches a list of all Dashboard.

        Returns:
        List: A list of all Dashboard.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        try:
            list_response = self._api_instance.v1beta2_dashboards_get()
            return list_response
        except ApiException as e:
            pprint(
                "Exception when calling DashboardsV1beta2Api->v1beta2_dashboards_get: %s\n" % e
            )
            raise e
