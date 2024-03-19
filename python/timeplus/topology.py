from pprint import pprint
import swagger_client
from swagger_client.rest import ApiException


class Topology:
    def __init__(self, env):
        """
        Initializes topology UDF object with the provided environment.

        Args:
        env: The environment in which the topology operates.
        """
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance = swagger_client.TopologyV1beta2Api(
            swagger_client.ApiClient(self._configuration)
        )

    def get(self):
        """
        Fetches a topology.

        Returns:
        List(swagger_client.models.view.View): A list of all views.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        try:
            response = self._api_instance.v1beta2_topology_get()
            return response
        except ApiException as e:
            pprint(
                "Exception when calling TopologyV1beta2Api->v1beta2_topology_get: %s\n"
                % e
            )
            raise e
