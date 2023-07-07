import swagger_client


class Environment:
    def __init__(self):
        """Constructor"""
        self._configuration = swagger_client.Configuration()
        self._workspace = None
        self._address = None

    def apikey(self, key):
        """
        Method to set the API key for the connection.

        Parameters:
        key: String - API key for the connection.

        Returns:
        Environment: The current Environment instance.
        """
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
        self._address = url
        if self._workspace:
            self._configuration.host = f"{self._address}/{self._workspace}/api"
        else:
            self._configuration.host = f"{self._address}/api"
        return self

    def _conf(self):
        """Internal method to get the current configuration."""
        return self._configuration
