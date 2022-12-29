import swagger_client


class Environment:
    def __init__(self):
        """Constructor"""
        self._configuration = swagger_client.Configuration()
        self._workspace = None
        self._address = None

    def apikey(self, key):
        self._configuration.api_key["X-Api-Key"] = key
        return self

    def workspace(self, name):
        self._workspace = name
        if not self._address:
            self._configuration.host = (
                f"https//beta.timeplus.cloud/{self._workspace}/api"
            )
        else:
            self._configuration.host = f"{self._address}/{self._workspace}/api"
        return self

    def address(self, url):
        self._address = url
        if self._workspace:
            self._configuration.host = f"{self._address}/{self._workspace}/api"
        else:
            self._configuration.host = f"{self._address}/api"
        return self

    def _conf(self):
        return self._configuration
