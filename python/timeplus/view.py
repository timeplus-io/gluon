from pprint import pprint
import swagger_client
from swagger_client.rest import ApiException


class View:
    def __init__(self, env):
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
        self._name = view_name
        return self

    def query(self, view_query):
        self._query = view_query
        return self

    def materialized(self, view_materialized):
        self._materialized = view_materialized
        return self

    def target_stream(self, view_target_stream):
        self._target_stream = view_target_stream
        return self

    def description(self, view_description):
        self._description = view_description
        return self

    def create(self):
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
        try:
            list_response = self._api_instance.v1beta2_views_get()
            return list_response
        except ApiException as e:
            pprint(
                "Exception when calling ViewsV1beta2Api->v1beta2_views_get: %s\n" % e
            )
            raise e

    def delete(self):
        self._api_instance.v1beta2_views_name_delete(self._name)

    def get(self):
        try:
            self._metadata = self._api_instance.v1beta2_viewsname_get(self._name)
        except ApiException as e:
            pprint(
                "Exception when calling ViewsV1beta2Api->v1beta2_viewsname_get: %s\n"
                % e
            )
            raise e

    def metadata(self):
        return self._metadata

    def exist(self):
        try:
            self.get()
            return True
        except Exception:
            return False
