import json
import sseclient

from pprint import pprint

import swagger_client
from swagger_client.rest import ApiException


class Query:
    def __init__(self, env):
        """
        Constructor for the Query class.

        Parameters:
        env: Environment - An instance of the Environment class.
        """
        self._env = env
        self._configuration = self._env._conf()
        self._api_instance = swagger_client.QueriesV1beta2Api(
            swagger_client.ApiClient(self._configuration)
        )
        self._create_response = None
        self._batching_policy = None
        self._metadata = {}

    def sql(self, query):
        """
        Method to set the SQL query.

        Parameters:
        query: String - The SQL query to be executed.

        Returns:
        Query: The current Query instance.
        """
        self._sql = query
        return self

    def batching_policy(self, count, time_ms):
        """
        Method to set the batching policy query.
        refer to https://docs.timeplus.com/rest.html#tag/Queries-v1beta2/paths/~1v1beta2~1queries/post

        Parameters:
        count: integer - The max result count per batch
        time_ms: interger - The max interval per batch in milliseconds

        Returns:
        Query: The current Query instance.
        """
        self._batching_policy = swagger_client.models.BatchingPolicy(
            count=count, time_ms=time_ms
        )
        return self

    def create(self):
        """
        Method to create the query.

        Returns:
        Query: The current Query instance.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        body = swagger_client.CreateQueryRequestV1Beta2(
            sql=self._sql, batching_policy=self._batching_policy
        )
        try:
            # as to support sse, the reponse is urllib3.response.HTTPResponse
            # instead of swagger_client.models.query.Query
            self._create_response = self._api_instance.v1beta2_queries_post(body)
            _sse_client = sseclient.SSEClient(self._create_response)
            self._events = _sse_client.events()
            self._query = next(self._events)
            self._metadata = json.loads(self._query.data)
            return self
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta2Api->v1beta2_queries_post: %s\n"
                % e
            )
            raise e

    def metadata(self):
        """
        Retrieve the internal api object

        Returns:
        Dict: json object of API object query.
        """

        return self._metadata

    def id(self, *args):
        if len(args) == 0:  # get id
            if "id" not in self._metadata:
                raise ApiException("id is not provided")
            return self._metadata["id"]
        elif len(args) == 1:  # set id
            new_value = args[0]
            self._metadata["id"] = new_value
            return self
        else:
            raise ApiException("id() accepts at most 1 argument")

        return self._metadata["id"]

    def header(self):
        return self._metadata["result"]["header"]

    def result(self):
        return self._events

    def delete(self):
        self._api_instance.v1beta2_queries_id_delete(self.id())

    def cancel(self):
        """
        Method to cancel the query.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        try:
            self._cancel_response = self._api_instance.v1beta2_queries_id_cancel_post(
                id=self.id()
            )
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta2Api->v1beta2_queries_id_cancel_post: %s\n"
                % e
            )
            raise e

    def get(self):
        """
        Method to get the query with the given ID.

        Parameters:
        id: String - The ID of the query.

        Returns:
        Query: The current Query instance.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        try:
            self._get_response = self._api_instance.v1beta2_queries_id_get(id=self.id())
            self._metadata = self._get_response
            return self
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta2Api->v1beta2_queries_id_get: %s\n"
                % e
            )
            raise e

    def list(self):
        """
         Method to get a list of all queries.

        Returns:
        List(swagger_client.models.query.Query): A list of all queries.

        Raises:
        ApiException: If an error occurs during the API call.
        """
        try:
            list_response = self._api_instance.v1beta2_queries_get()
            return list_response
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta2Api->v1beta2_queries_get: %s\n"
                % e
            )
            raise e

    def analyze(self):
        """
        Method to analyze the SQL query.

        Returns:
        JSON: The result of the analysis.

        Raises:
        ApiException: If an error occurs during the API call or if no SQL is provided.
        """
        if self._sql is None:
            raise ApiException("sql must be provided")

        body = swagger_client.AnalyzeSQLRequest(sql=self._sql)
        try:
            analyze_response = self._api_instance.v1beta2_sqlanalyze_post(body)
            return analyze_response
        except ApiException as e:
            pprint(
                "Exception when calling QueriesV1beta2Api->v1beta2_sqlanalyze_post: %s\n"
                % e
            )
            raise e
