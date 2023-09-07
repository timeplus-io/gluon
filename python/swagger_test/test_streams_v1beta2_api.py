# coding: utf-8

"""
    Timeplus

    Welcome to the Timeplus HTTP REST API specification.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@timeplus.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.timeplus.streams_v1beta2_api import StreamsV1beta2Api  # noqa: E501
from swagger_client.rest import ApiException


class TestStreamsV1beta2Api(unittest.TestCase):
    """StreamsV1beta2Api unit test stubs"""

    def setUp(self):
        self.api = StreamsV1beta2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1beta2_streams_external_post(self):
        """Test case for v1beta2_streams_external_post

        create an external stream  # noqa: E501
        """
        pass

    def test_v1beta2_streams_get(self):
        """Test case for v1beta2_streams_get

        list streams  # noqa: E501
        """
        pass

    def test_v1beta2_streams_name_delete(self):
        """Test case for v1beta2_streams_name_delete

        delete a stream  # noqa: E501
        """
        pass

    def test_v1beta2_streams_name_get(self):
        """Test case for v1beta2_streams_name_get

        get a stream  # noqa: E501
        """
        pass

    def test_v1beta2_streams_name_ingest_post(self):
        """Test case for v1beta2_streams_name_ingest_post

        ingest data  # noqa: E501
        """
        pass

    def test_v1beta2_streams_name_patch(self):
        """Test case for v1beta2_streams_name_patch

        update a stream  # noqa: E501
        """
        pass

    def test_v1beta2_streams_name_stats_get(self):
        """Test case for v1beta2_streams_name_stats_get

        get the stats of a stream  # noqa: E501
        """
        pass

    def test_v1beta2_streams_post(self):
        """Test case for v1beta2_streams_post

        create a stream  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
