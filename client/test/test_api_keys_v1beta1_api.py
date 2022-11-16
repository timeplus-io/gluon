# coding: utf-8

"""
    Timeplus

    Welcome to the Timeplus HTTP REST API specification.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: support@timeplus.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import timeplus_client
from timeplus_client.api.api_keys_v1beta1_api import APIKeysV1beta1Api  # noqa: E501
from timeplus_client.rest import ApiException


class TestAPIKeysV1beta1Api(unittest.TestCase):
    """APIKeysV1beta1Api unit test stubs"""

    def setUp(self):
        self.api = APIKeysV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1beta1_auth_api_keys_get(self):
        """Test case for v1beta1_auth_api_keys_get

        List API keys  # noqa: E501
        """
        pass

    def test_v1beta1_auth_api_keys_id_delete(self):
        """Test case for v1beta1_auth_api_keys_id_delete

        Delete an API key  # noqa: E501
        """
        pass

    def test_v1beta1_auth_api_keys_post(self):
        """Test case for v1beta1_auth_api_keys_post

        Create an API key  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
