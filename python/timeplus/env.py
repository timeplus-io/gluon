import swagger_client

WORKSPACE_LEN = 8
APIKEY_LEN = 60
DEV_ADDRESS = "https://dev.timeplus.cloud"


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
        self._workspace = name
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

    def username(self, value):
        """
        Method to set the username for the connection.

        Parameters:
        value: String - username.

        Returns:
        Environment: The current Environment instance.
        """
        self._configuration.username = value
        return self

    def password(self, value):
        """
        Method to set the password for the connection.

        Parameters:
        value: String - user password.

        Returns:
        Environment: The current Environment instance.
        """
        self._configuration.password = value
        return self

    def _conf(self):
        """Internal method to get the current configuration."""
        return self._configuration
