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

class BatchingPolicy(object):
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
        'count': 'int',
        'time_ms': 'int'
    }

    attribute_map = {
        'count': 'count',
        'time_ms': 'time_ms'
    }

    def __init__(self, count=None, time_ms=None):  # noqa: E501
        """BatchingPolicy - a model defined in Swagger"""  # noqa: E501
        self._count = None
        self._time_ms = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if time_ms is not None:
            self.time_ms = time_ms

    @property
    def count(self):
        """Gets the count of this BatchingPolicy.  # noqa: E501

        The max result count per batch  # noqa: E501

        :return: The count of this BatchingPolicy.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchingPolicy.

        The max result count per batch  # noqa: E501

        :param count: The count of this BatchingPolicy.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def time_ms(self):
        """Gets the time_ms of this BatchingPolicy.  # noqa: E501

        The max interval per batch in milliseconds  # noqa: E501

        :return: The time_ms of this BatchingPolicy.  # noqa: E501
        :rtype: int
        """
        return self._time_ms

    @time_ms.setter
    def time_ms(self, time_ms):
        """Sets the time_ms of this BatchingPolicy.

        The max interval per batch in milliseconds  # noqa: E501

        :param time_ms: The time_ms of this BatchingPolicy.  # noqa: E501
        :type: int
        """

        self._time_ms = time_ms

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
        if issubclass(BatchingPolicy, dict):
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
        if not isinstance(other, BatchingPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
