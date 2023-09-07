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

class SinkStats(object):
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
        'earliest_event': 'str',
        'errors': 'list[StatsError]',
        'failure_count': 'float',
        'historical_data_bytes': 'int',
        'latest_event': 'str',
        'row_count': 'int',
        'streaming_data_bytes': 'int',
        'success_count': 'float',
        'throughput': 'list[StatsThroughput]'
    }

    attribute_map = {
        'earliest_event': 'earliest_event',
        'errors': 'errors',
        'failure_count': 'failure_count',
        'historical_data_bytes': 'historical_data_bytes',
        'latest_event': 'latest_event',
        'row_count': 'row_count',
        'streaming_data_bytes': 'streaming_data_bytes',
        'success_count': 'success_count',
        'throughput': 'throughput'
    }

    def __init__(self, earliest_event=None, errors=None, failure_count=None, historical_data_bytes=None, latest_event=None, row_count=None, streaming_data_bytes=None, success_count=None, throughput=None):  # noqa: E501
        """SinkStats - a model defined in Swagger"""  # noqa: E501
        self._earliest_event = None
        self._errors = None
        self._failure_count = None
        self._historical_data_bytes = None
        self._latest_event = None
        self._row_count = None
        self._streaming_data_bytes = None
        self._success_count = None
        self._throughput = None
        self.discriminator = None
        if earliest_event is not None:
            self.earliest_event = earliest_event
        self.errors = errors
        self.failure_count = failure_count
        if historical_data_bytes is not None:
            self.historical_data_bytes = historical_data_bytes
        if latest_event is not None:
            self.latest_event = latest_event
        if row_count is not None:
            self.row_count = row_count
        if streaming_data_bytes is not None:
            self.streaming_data_bytes = streaming_data_bytes
        self.success_count = success_count
        self.throughput = throughput

    @property
    def earliest_event(self):
        """Gets the earliest_event of this SinkStats.  # noqa: E501


        :return: The earliest_event of this SinkStats.  # noqa: E501
        :rtype: str
        """
        return self._earliest_event

    @earliest_event.setter
    def earliest_event(self, earliest_event):
        """Sets the earliest_event of this SinkStats.


        :param earliest_event: The earliest_event of this SinkStats.  # noqa: E501
        :type: str
        """

        self._earliest_event = earliest_event

    @property
    def errors(self):
        """Gets the errors of this SinkStats.  # noqa: E501

        It only contains the latest error of the pipeline  # noqa: E501

        :return: The errors of this SinkStats.  # noqa: E501
        :rtype: list[StatsError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this SinkStats.

        It only contains the latest error of the pipeline  # noqa: E501

        :param errors: The errors of this SinkStats.  # noqa: E501
        :type: list[StatsError]
        """
        if errors is None:
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def failure_count(self):
        """Gets the failure_count of this SinkStats.  # noqa: E501


        :return: The failure_count of this SinkStats.  # noqa: E501
        :rtype: float
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        """Sets the failure_count of this SinkStats.


        :param failure_count: The failure_count of this SinkStats.  # noqa: E501
        :type: float
        """
        if failure_count is None:
            raise ValueError("Invalid value for `failure_count`, must not be `None`")  # noqa: E501

        self._failure_count = failure_count

    @property
    def historical_data_bytes(self):
        """Gets the historical_data_bytes of this SinkStats.  # noqa: E501


        :return: The historical_data_bytes of this SinkStats.  # noqa: E501
        :rtype: int
        """
        return self._historical_data_bytes

    @historical_data_bytes.setter
    def historical_data_bytes(self, historical_data_bytes):
        """Sets the historical_data_bytes of this SinkStats.


        :param historical_data_bytes: The historical_data_bytes of this SinkStats.  # noqa: E501
        :type: int
        """

        self._historical_data_bytes = historical_data_bytes

    @property
    def latest_event(self):
        """Gets the latest_event of this SinkStats.  # noqa: E501


        :return: The latest_event of this SinkStats.  # noqa: E501
        :rtype: str
        """
        return self._latest_event

    @latest_event.setter
    def latest_event(self, latest_event):
        """Sets the latest_event of this SinkStats.


        :param latest_event: The latest_event of this SinkStats.  # noqa: E501
        :type: str
        """

        self._latest_event = latest_event

    @property
    def row_count(self):
        """Gets the row_count of this SinkStats.  # noqa: E501


        :return: The row_count of this SinkStats.  # noqa: E501
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this SinkStats.


        :param row_count: The row_count of this SinkStats.  # noqa: E501
        :type: int
        """

        self._row_count = row_count

    @property
    def streaming_data_bytes(self):
        """Gets the streaming_data_bytes of this SinkStats.  # noqa: E501


        :return: The streaming_data_bytes of this SinkStats.  # noqa: E501
        :rtype: int
        """
        return self._streaming_data_bytes

    @streaming_data_bytes.setter
    def streaming_data_bytes(self, streaming_data_bytes):
        """Sets the streaming_data_bytes of this SinkStats.


        :param streaming_data_bytes: The streaming_data_bytes of this SinkStats.  # noqa: E501
        :type: int
        """

        self._streaming_data_bytes = streaming_data_bytes

    @property
    def success_count(self):
        """Gets the success_count of this SinkStats.  # noqa: E501


        :return: The success_count of this SinkStats.  # noqa: E501
        :rtype: float
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this SinkStats.


        :param success_count: The success_count of this SinkStats.  # noqa: E501
        :type: float
        """
        if success_count is None:
            raise ValueError("Invalid value for `success_count`, must not be `None`")  # noqa: E501

        self._success_count = success_count

    @property
    def throughput(self):
        """Gets the throughput of this SinkStats.  # noqa: E501

        Each data point represents the average throughput for one minute  # noqa: E501

        :return: The throughput of this SinkStats.  # noqa: E501
        :rtype: list[StatsThroughput]
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this SinkStats.

        Each data point represents the average throughput for one minute  # noqa: E501

        :param throughput: The throughput of this SinkStats.  # noqa: E501
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
        if issubclass(SinkStats, dict):
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
        if not isinstance(other, SinkStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
