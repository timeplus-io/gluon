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

class GlobalMetricsResult(object):
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
        'name': 'str',
        'time': 'str',
        'value': 'float'
    }

    attribute_map = {
        'name': 'name',
        'time': 'time',
        'value': 'value'
    }

    def __init__(self, name=None, time=None, value=None):  # noqa: E501
        """GlobalMetricsResult - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._time = None
        self._value = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if time is not None:
            self.time = time
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this GlobalMetricsResult.  # noqa: E501


        :return: The name of this GlobalMetricsResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlobalMetricsResult.


        :param name: The name of this GlobalMetricsResult.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def time(self):
        """Gets the time of this GlobalMetricsResult.  # noqa: E501


        :return: The time of this GlobalMetricsResult.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this GlobalMetricsResult.


        :param time: The time of this GlobalMetricsResult.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def value(self):
        """Gets the value of this GlobalMetricsResult.  # noqa: E501


        :return: The value of this GlobalMetricsResult.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GlobalMetricsResult.


        :param value: The value of this GlobalMetricsResult.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if issubclass(GlobalMetricsResult, dict):
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
        if not isinstance(other, GlobalMetricsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
