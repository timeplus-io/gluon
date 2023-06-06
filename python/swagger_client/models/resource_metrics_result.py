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

class ResourceMetricsResult(object):
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
        'failure_count': 'float',
        'id': 'str',
        'success_count': 'float',
        'throughput': 'list[MetricsQueryThroughput]'
    }

    attribute_map = {
        'failure_count': 'failure_count',
        'id': 'id',
        'success_count': 'success_count',
        'throughput': 'throughput'
    }

    def __init__(self, failure_count=None, id=None, success_count=None, throughput=None):  # noqa: E501
        """ResourceMetricsResult - a model defined in Swagger"""  # noqa: E501
        self._failure_count = None
        self._id = None
        self._success_count = None
        self._throughput = None
        self.discriminator = None
        self.failure_count = failure_count
        self.id = id
        self.success_count = success_count
        self.throughput = throughput

    @property
    def failure_count(self):
        """Gets the failure_count of this ResourceMetricsResult.  # noqa: E501


        :return: The failure_count of this ResourceMetricsResult.  # noqa: E501
        :rtype: float
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        """Sets the failure_count of this ResourceMetricsResult.


        :param failure_count: The failure_count of this ResourceMetricsResult.  # noqa: E501
        :type: float
        """
        if failure_count is None:
            raise ValueError("Invalid value for `failure_count`, must not be `None`")  # noqa: E501

        self._failure_count = failure_count

    @property
    def id(self):
        """Gets the id of this ResourceMetricsResult.  # noqa: E501


        :return: The id of this ResourceMetricsResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceMetricsResult.


        :param id: The id of this ResourceMetricsResult.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def success_count(self):
        """Gets the success_count of this ResourceMetricsResult.  # noqa: E501


        :return: The success_count of this ResourceMetricsResult.  # noqa: E501
        :rtype: float
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this ResourceMetricsResult.


        :param success_count: The success_count of this ResourceMetricsResult.  # noqa: E501
        :type: float
        """
        if success_count is None:
            raise ValueError("Invalid value for `success_count`, must not be `None`")  # noqa: E501

        self._success_count = success_count

    @property
    def throughput(self):
        """Gets the throughput of this ResourceMetricsResult.  # noqa: E501


        :return: The throughput of this ResourceMetricsResult.  # noqa: E501
        :rtype: list[MetricsQueryThroughput]
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this ResourceMetricsResult.


        :param throughput: The throughput of this ResourceMetricsResult.  # noqa: E501
        :type: list[MetricsQueryThroughput]
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
        if issubclass(ResourceMetricsResult, dict):
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
        if not isinstance(other, ResourceMetricsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other