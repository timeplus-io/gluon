# coding: utf-8

"""
    Timeplus

    Welcome to the Timeplus HTTP REST API specification.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@timeplus.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdateViewRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'str',
        'logstore_retention_bytes': 'int',
        'logstore_retention_ms': 'int',
        'query': 'str',
        'ttl_expression': 'str'
    }

    attribute_map = {
        'description': 'description',
        'logstore_retention_bytes': 'logstore_retention_bytes',
        'logstore_retention_ms': 'logstore_retention_ms',
        'query': 'query',
        'ttl_expression': 'ttl_expression'
    }

    def __init__(self, description=None, logstore_retention_bytes=None, logstore_retention_ms=None, query=None, ttl_expression=None):  # noqa: E501
        """UpdateViewRequest - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._logstore_retention_bytes = None
        self._logstore_retention_ms = None
        self._query = None
        self._ttl_expression = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if logstore_retention_bytes is not None:
            self.logstore_retention_bytes = logstore_retention_bytes
        if logstore_retention_ms is not None:
            self.logstore_retention_ms = logstore_retention_ms
        if query is not None:
            self.query = query
        if ttl_expression is not None:
            self.ttl_expression = ttl_expression

    @property
    def description(self):
        """Gets the description of this UpdateViewRequest.  # noqa: E501


        :return: The description of this UpdateViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateViewRequest.


        :param description: The description of this UpdateViewRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def logstore_retention_bytes(self):
        """Gets the logstore_retention_bytes of this UpdateViewRequest.  # noqa: E501

        The max size a stream can grow. Defaulted to 10 GiB  # noqa: E501

        :return: The logstore_retention_bytes of this UpdateViewRequest.  # noqa: E501
        :rtype: int
        """
        return self._logstore_retention_bytes

    @logstore_retention_bytes.setter
    def logstore_retention_bytes(self, logstore_retention_bytes):
        """Sets the logstore_retention_bytes of this UpdateViewRequest.

        The max size a stream can grow. Defaulted to 10 GiB  # noqa: E501

        :param logstore_retention_bytes: The logstore_retention_bytes of this UpdateViewRequest.  # noqa: E501
        :type: int
        """

        self._logstore_retention_bytes = logstore_retention_bytes

    @property
    def logstore_retention_ms(self):
        """Gets the logstore_retention_ms of this UpdateViewRequest.  # noqa: E501

        The max time the data can be retained in the stream. Defaulted to 7 days  # noqa: E501

        :return: The logstore_retention_ms of this UpdateViewRequest.  # noqa: E501
        :rtype: int
        """
        return self._logstore_retention_ms

    @logstore_retention_ms.setter
    def logstore_retention_ms(self, logstore_retention_ms):
        """Sets the logstore_retention_ms of this UpdateViewRequest.

        The max time the data can be retained in the stream. Defaulted to 7 days  # noqa: E501

        :param logstore_retention_ms: The logstore_retention_ms of this UpdateViewRequest.  # noqa: E501
        :type: int
        """

        self._logstore_retention_ms = logstore_retention_ms

    @property
    def query(self):
        """Gets the query of this UpdateViewRequest.  # noqa: E501


        :return: The query of this UpdateViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this UpdateViewRequest.


        :param query: The query of this UpdateViewRequest.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def ttl_expression(self):
        """Gets the ttl_expression of this UpdateViewRequest.  # noqa: E501


        :return: The ttl_expression of this UpdateViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._ttl_expression

    @ttl_expression.setter
    def ttl_expression(self, ttl_expression):
        """Sets the ttl_expression of this UpdateViewRequest.


        :param ttl_expression: The ttl_expression of this UpdateViewRequest.  # noqa: E501
        :type: str
        """

        self._ttl_expression = ttl_expression

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateViewRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateViewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other