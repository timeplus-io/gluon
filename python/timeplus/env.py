import swagger_client


class Environment:
    def __init__(self):
        """Constructor"""
        self._configuration = swagger_client.Configuration()

    def apikey(self, key):
        self._configuration.api_key["X-Api-Key"] = key
        return self

    def workspace(self, name):
        self.workspace = name
        if not self.address:
            self._configuration.host = (
                f"https//beta.timeplus.cloud/{self.workspace}/api"
            )
        else:
            self._configuration.host = f"{self.address}/{self.workspace}/api"
        return self

    def address(self, url):
        self.address = url
        if self.workspace:
            self._configuration.host = f"{self.address}/{self.workspace}/api"
        else:
            self._configuration.host = f"{self.address}/default/api"
        return self

    def _conf(self):
        return self._configuration
