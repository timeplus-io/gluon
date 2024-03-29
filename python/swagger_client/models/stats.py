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

class Stats(object):
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
        'errors': 'list[StatsError]',
        'failure_count': 'float',
        'success_count': 'float',
        'throughput': 'list[StatsThroughput]'
    }

    attribute_map = {
        'errors': 'errors',
        'failure_count': 'failure_count',
        'success_count': 'success_count',
        'throughput': 'throughput'
    }

    def __init__(self, errors=None, failure_count=None, success_count=None, throughput=None):  # noqa: E501
        """Stats - a model defined in Swagger"""  # noqa: E501
        self._errors = None
        self._failure_count = None
        self._success_count = None
        self._throughput = None
        self.discriminator = None
        self.errors = errors
        self.failure_count = failure_count
        self.success_count = success_count
        self.throughput = throughput

    @property
    def errors(self):
        """Gets the errors of this Stats.  # noqa: E501

        It only contains the latest error of the pipeline  # noqa: E501

        :return: The errors of this Stats.  # noqa: E501
        :rtype: list[StatsError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Stats.

        It only contains the latest error of the pipeline  # noqa: E501

        :param errors: The errors of this Stats.  # noqa: E501
        :type: list[StatsError]
        """
        if errors is None:
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def failure_count(self):
        """Gets the failure_count of this Stats.  # noqa: E501


        :return: The failure_count of this Stats.  # noqa: E501
        :rtype: float
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        """Sets the failure_count of this Stats.


        :param failure_count: The failure_count of this Stats.  # noqa: E501
        :type: float
        """
        if failure_count is None:
            raise ValueError("Invalid value for `failure_count`, must not be `None`")  # noqa: E501

        self._failure_count = failure_count

    @property
    def success_count(self):
        """Gets the success_count of this Stats.  # noqa: E501


        :return: The success_count of this Stats.  # noqa: E501
        :rtype: float
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this Stats.


        :param success_count: The success_count of this Stats.  # noqa: E501
        :type: float
        """
        if success_count is None:
            raise ValueError("Invalid value for `success_count`, must not be `None`")  # noqa: E501

        self._success_count = success_count

    @property
    def throughput(self):
        """Gets the throughput of this Stats.  # noqa: E501

        Each data point represents the average throughput for one minute  # noqa: E501

        :return: The throughput of this Stats.  # noqa: E501
        :rtype: list[StatsThroughput]
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this Stats.

        Each data point represents the average throughput for one minute  # noqa: E501

        :param throughput: The throughput of this Stats.  # noqa: E501
        :type: list[StatsThroughput]
        """
        if throughput is None:
            raise ValueError("Invalid value for `throughput`, must not be `None`")  # noqa: E501

        self._throughput = throughput

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
        if issubclass(Stats, dict):
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
        if not isinstance(other, Stats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
