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
from swagger_client.timeplus.alerts_internal_api import AlertsInternalApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAlertsInternalApi(unittest.TestCase):
    """AlertsInternalApi unit test stubs"""

    def setUp(self):
        self.api = AlertsInternalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_internal_tenants_tenant_alerts_id_start_post(self):
        """Test case for api_internal_tenants_tenant_alerts_id_start_post

        start an alert.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()