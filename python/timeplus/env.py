import swagger_client

WORKSPACE_LEN = 8
APIKEY_LEN = 60


class Environment:
    def __init__(self):
        """Constructor"""
        self._configuration = swagger_client.Configuration()
        self._workspace = None
        self._address = "https://us.timeplus.cloud"

    def apikey(self, key):
        """
        Method to set the API key for the connection.

        Parameters:
        key: String - API key for the connection.

        Returns:
        Environment: The current Environment instance.
        """
        print(f"api key is {key}")
        if len(key) != APIKEY_LEN:
            raise ValueError(f"The apikey should be {APIKEY_LEN} characters")
        self._configuration.api_key["X-Api-Key"] = key
        return self

    def workspace(self, name):
        """
        Method to set the workspace for the connection.

        Parameters:
        name: String - Workspace name.

        Returns:
        Environment: The current Environment instance.
        """
        if len(name) != WORKSPACE_LEN:
            raise ValueError(
                f"Did you set the workspace name? Please set the workspace ID (usually {WORKSPACE_LEN} characters long)")
        self._workspace = name
        if not self._address:
            self._configuration.host = f"https//us.timeplus.cloud/{self._workspace}/api"
        else:
            self._configuration.host = f"{self._address}/{self._workspace}/api"
        return self

    def address(self, url):
        """
        Method to set the address for the connection.

        Parameters:
        url: String - Server address.

        Returns:
        Environment: The current Environment instance.
        """
        self._address = url.rstrip("/")
        if self._workspace:
            self._configuration.host = f"{self._address}/{self._workspace}/api"
        else:
            self._configuration.host = f"{self._address}/api"
        return self

    def _conf(self):
        """Internal method to get the current configuration."""
        return self._configuration
