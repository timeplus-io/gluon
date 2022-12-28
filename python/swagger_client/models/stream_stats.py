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

class StreamStats(object):
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
        'historical_data_bytes': 'int',
        'row_count': 'int',
        'streaming_data_bytes': 'int'
    }

    attribute_map = {
        'historical_data_bytes': 'historical_data_bytes',
        'row_count': 'row_count',
        'streaming_data_bytes': 'streaming_data_bytes'
    }

    def __init__(self, historical_data_bytes=None, row_count=None, streaming_data_bytes=None):  # noqa: E501
        """StreamStats - a model defined in Swagger"""  # noqa: E501
        self._historical_data_bytes = None
        self._row_count = None
        self._streaming_data_bytes = None
        self.discriminator = None
        if historical_data_bytes is not None:
            self.historical_data_bytes = historical_data_bytes
        if row_count is not None:
            self.row_count = row_count
        if streaming_data_bytes is not None:
            self.streaming_data_bytes = streaming_data_bytes

    @property
    def historical_data_bytes(self):
        """Gets the historical_data_bytes of this StreamStats.  # noqa: E501


        :return: The historical_data_bytes of this StreamStats.  # noqa: E501
        :rtype: int
        """
        return self._historical_data_bytes

    @historical_data_bytes.setter
    def historical_data_bytes(self, historical_data_bytes):
        """Sets the historical_data_bytes of this StreamStats.


        :param historical_data_bytes: The historical_data_bytes of this StreamStats.  # noqa: E501
        :type: int
        """

        self._historical_data_bytes = historical_data_bytes

    @property
    def row_count(self):
        """Gets the row_count of this StreamStats.  # noqa: E501


        :return: The row_count of this StreamStats.  # noqa: E501
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this StreamStats.


        :param row_count: The row_count of this StreamStats.  # noqa: E501
        :type: int
        """

        self._row_count = row_count

    @property
    def streaming_data_bytes(self):
        """Gets the streaming_data_bytes of this StreamStats.  # noqa: E501


        :return: The streaming_data_bytes of this StreamStats.  # noqa: E501
        :rtype: int
        """
        return self._streaming_data_bytes

    @streaming_data_bytes.setter
    def streaming_data_bytes(self, streaming_data_bytes):
        """Sets the streaming_data_bytes of this StreamStats.


        :param streaming_data_bytes: The streaming_data_bytes of this StreamStats.  # noqa: E501
        :type: int
        """

        self._streaming_data_bytes = streaming_data_bytes

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
        if issubclass(StreamStats, dict):
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
        if not isinstance(other, StreamStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
