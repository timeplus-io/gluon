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
from timeplus_client.api.streams_v1beta1_api import StreamsV1beta1Api  # noqa: E501
from timeplus_client.rest import ApiException


class TestStreamsV1beta1Api(unittest.TestCase):
    """StreamsV1beta1Api unit test stubs"""

    def setUp(self):
        self.api = StreamsV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1beta1_streams_external_post(self):
        """Test case for v1beta1_streams_external_post

        create an external stream.  # noqa: E501
        """
        pass

    def test_v1beta1_streams_get(self):
        """Test case for v1beta1_streams_get

        list streams.  # noqa: E501
        """
        pass

    def test_v1beta1_streams_name_delete(self):
        """Test case for v1beta1_streams_name_delete

        delete a stream.  # noqa: E501
        """
        pass

    def test_v1beta1_streams_name_ingest_post(self):
        """Test case for v1beta1_streams_name_ingest_post

        ingest data.  # noqa: E501
        """
        pass

    def test_v1beta1_streams_name_put(self):
        """Test case for v1beta1_streams_name_put

        Update a stream.  # noqa: E501
        """
        pass

    def test_v1beta1_streams_post(self):
        """Test case for v1beta1_streams_post

        create a stream.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()