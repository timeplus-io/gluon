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

class StreamDef(object):
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
        'columns': 'list[ColumnDef]',
        'description': 'str',
        'event_time_column': 'str',
        'event_time_timezone': 'str',
        'logstore_retention_bytes': 'int',
        'logstore_retention_ms': 'int',
        'mode': 'str',
        'name': 'str',
        'order_by_expression': 'str',
        'order_by_granularity': 'str',
        'partition_by_granularity': 'str',
        'primary_key': 'str',
        'replication_factor': 'int',
        'shards': 'int',
        'ttl_expression': 'str'
    }

    attribute_map = {
        'columns': 'columns',
        'description': 'description',
        'event_time_column': 'event_time_column',
        'event_time_timezone': 'event_time_timezone',
        'logstore_retention_bytes': 'logstore_retention_bytes',
        'logstore_retention_ms': 'logstore_retention_ms',
        'mode': 'mode',
        'name': 'name',
        'order_by_expression': 'order_by_expression',
        'order_by_granularity': 'order_by_granularity',
        'partition_by_granularity': 'partition_by_granularity',
        'primary_key': 'primary_key',
        'replication_factor': 'replication_factor',
        'shards': 'shards',
        'ttl_expression': 'ttl_expression'
    }

    def __init__(self, columns=None, description=None, event_time_column=None, event_time_timezone=None, logstore_retention_bytes=None, logstore_retention_ms=None, mode=None, name=None, order_by_expression=None, order_by_granularity=None, partition_by_granularity=None, primary_key=None, replication_factor=None, shards=None, ttl_expression=None):  # noqa: E501
        """StreamDef - a model defined in Swagger"""  # noqa: E501
        self._columns = None
        self._description = None
        self._event_time_column = None
        self._event_time_timezone = None
        self._logstore_retention_bytes = None
        self._logstore_retention_ms = None
        self._mode = None
        self._name = None
        self._order_by_expression = None
        self._order_by_granularity = None
        self._partition_by_granularity = None
        self._primary_key = None
        self._replication_factor = None
        self._shards = None
        self._ttl_expression = None
        self.discriminator = None
        if columns is not None:
            self.columns = columns
        if description is not None:
            self.description = description
        if event_time_column is not None:
            self.event_time_column = event_time_column
        if event_time_timezone is not None:
            self.event_time_timezone = event_time_timezone
        if logstore_retention_bytes is not None:
            self.logstore_retention_bytes = logstore_retention_bytes
        if logstore_retention_ms is not None:
            self.logstore_retention_ms = logstore_retention_ms
        if mode is not None:
            self.mode = mode
        self.name = name
        if order_by_expression is not None:
            self.order_by_expression = order_by_expression
        if order_by_granularity is not None:
            self.order_by_granularity = order_by_granularity
        if partition_by_granularity is not None:
            self.partition_by_granularity = partition_by_granularity
        if primary_key is not None:
            self.primary_key = primary_key
        if replication_factor is not None:
            self.replication_factor = replication_factor
        if shards is not None:
            self.shards = shards
        if ttl_expression is not None:
            self.ttl_expression = ttl_expression

    @property
    def columns(self):
        """Gets the columns of this StreamDef.  # noqa: E501


        :return: The columns of this StreamDef.  # noqa: E501
        :rtype: list[ColumnDef]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this StreamDef.


        :param columns: The columns of this StreamDef.  # noqa: E501
        :type: list[ColumnDef]
        """

        self._columns = columns

    @property
    def description(self):
        """Gets the description of this StreamDef.  # noqa: E501


        :return: The description of this StreamDef.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StreamDef.


        :param description: The description of this StreamDef.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def event_time_column(self):
        """Gets the event_time_column of this StreamDef.  # noqa: E501

        This column will be used as the event time if specified  # noqa: E501

        :return: The event_time_column of this StreamDef.  # noqa: E501
        :rtype: str
        """
        return self._event_time_column

    @event_time_column.setter
    def event_time_column(self, event_time_column):
        """Sets the event_time_column of this StreamDef.

        This column will be used as the event time if specified  # noqa: E501

        :param event_time_column: The event_time_column of this StreamDef.  # noqa: E501
        :type: str
        """

        self._event_time_column = event_time_column

    @property
    def event_time_timezone(self):
        """Gets the event_time_timezone of this StreamDef.  # noqa: E501

        The timezone of the `TimestampColumn`  # noqa: E501

        :return: The event_time_timezone of this StreamDef.  # noqa: E501
        :rtype: str
        """
        return self._event_time_timezone

    @event_time_timezone.setter
    def event_time_timezone(self, event_time_timezone):
        """Sets the event_time_timezone of this StreamDef.

        The timezone of the `TimestampColumn`  # noqa: E501

        :param event_time_timezone: The event_time_timezone of this StreamDef.  # noqa: E501
        :type: str
        """

        self._event_time_timezone = event_time_timezone

    @property
    def logstore_retention_bytes(self):
        """Gets the logstore_retention_bytes of this StreamDef.  # noqa: E501

        The max size a stream can grow. Any non-positive value means unlimited size. Defaulted to 10 GiB.  # noqa: E501

        :return: The logstore_retention_bytes of this StreamDef.  # noqa: E501
        :rtype: int
        """
        return self._logstore_retention_bytes

    @logstore_retention_bytes.setter
    def logstore_retention_bytes(self, logstore_retention_bytes):
        """Sets the logstore_retention_bytes of this StreamDef.

        The max size a stream can grow. Any non-positive value means unlimited size. Defaulted to 10 GiB.  # noqa: E501

        :param logstore_retention_bytes: The logstore_retention_bytes of this StreamDef.  # noqa: E501
        :type: int
        """

        self._logstore_retention_bytes = logstore_retention_bytes

    @property
    def logstore_retention_ms(self):
        """Gets the logstore_retention_ms of this StreamDef.  # noqa: E501

        The max time the data can be retained in the stream. Any non-positive value means unlimited time. Defaulted to 7 days.  # noqa: E501

        :return: The logstore_retention_ms of this StreamDef.  # noqa: E501
        :rtype: int
        """
        return self._logstore_retention_ms

    @logstore_retention_ms.setter
    def logstore_retention_ms(self, logstore_retention_ms):
        """Sets the logstore_retention_ms of this StreamDef.

        The max time the data can be retained in the stream. Any non-positive value means unlimited time. Defaulted to 7 days.  # noqa: E501

        :param logstore_retention_ms: The logstore_retention_ms of this StreamDef.  # noqa: E501
        :type: int
        """

        self._logstore_retention_ms = logstore_retention_ms

    @property
    def mode(self):
        """Gets the mode of this StreamDef.  # noqa: E501

        Storage mode of stream. Defaulted to `append`.  # noqa: E501

        :return: The mode of this StreamDef.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this StreamDef.

        Storage mode of stream. Defaulted to `append`.  # noqa: E501

        :param mode: The mode of this StreamDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["append", "changelog", "changelog_kv", "versioned_kv"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def name(self):
        """Gets the name of this StreamDef.  # noqa: E501

        Stream name should only contain a maximum of 64 letters, numbers, or _, and start with a letter  # noqa: E501

        :return: The name of this StreamDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StreamDef.

        Stream name should only contain a maximum of 64 letters, numbers, or _, and start with a letter  # noqa: E501

        :param name: The name of this StreamDef.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def order_by_expression(self):
        """Gets the order_by_expression of this StreamDef.  # noqa: E501


        :return: The order_by_expression of this StreamDef.  # noqa: E501
        :rtype: str
        """
        return self._order_by_expression

    @order_by_expression.setter
    def order_by_expression(self, order_by_expression):
        """Sets the order_by_expression of this StreamDef.


        :param order_by_expression: The order_by_expression of this StreamDef.  # noqa: E501
        :type: str
        """

        self._order_by_expression = order_by_expression

    @property
    def order_by_granularity(self):
        """Gets the order_by_granularity of this StreamDef.  # noqa: E501


        :return: The order_by_granularity of this StreamDef.  # noqa: E501
        :rtype: str
        """
        return self._order_by_granularity

    @order_by_granularity.setter
    def order_by_granularity(self, order_by_granularity):
        """Sets the order_by_granularity of this StreamDef.


        :param order_by_granularity: The order_by_granularity of this StreamDef.  # noqa: E501
        :type: str
        """

        self._order_by_granularity = order_by_granularity

    @property
    def partition_by_granularity(self):
        """Gets the partition_by_granularity of this StreamDef.  # noqa: E501


        :return: The partition_by_granularity of this StreamDef.  # noqa: E501
        :rtype: str
        """
        return self._partition_by_granularity

    @partition_by_granularity.setter
    def partition_by_granularity(self, partition_by_granularity):
        """Sets the partition_by_granularity of this StreamDef.


        :param partition_by_granularity: The partition_by_granularity of this StreamDef.  # noqa: E501
        :type: str
        """

        self._partition_by_granularity = partition_by_granularity

    @property
    def primary_key(self):
        """Gets the primary_key of this StreamDef.  # noqa: E501

        Expression of primary key, required in `changelog_kv` and `versioned_kv` mode  # noqa: E501

        :return: The primary_key of this StreamDef.  # noqa: E501
        :rtype: str
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """Sets the primary_key of this StreamDef.

        Expression of primary key, required in `changelog_kv` and `versioned_kv` mode  # noqa: E501

        :param primary_key: The primary_key of this StreamDef.  # noqa: E501
        :type: str
        """

        self._primary_key = primary_key

    @property
    def replication_factor(self):
        """Gets the replication_factor of this StreamDef.  # noqa: E501


        :return: The replication_factor of this StreamDef.  # noqa: E501
        :rtype: int
        """
        return self._replication_factor

    @replication_factor.setter
    def replication_factor(self, replication_factor):
        """Sets the replication_factor of this StreamDef.


        :param replication_factor: The replication_factor of this StreamDef.  # noqa: E501
        :type: int
        """

        self._replication_factor = replication_factor

    @property
    def shards(self):
        """Gets the shards of this StreamDef.  # noqa: E501


        :return: The shards of this StreamDef.  # noqa: E501
        :rtype: int
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        """Sets the shards of this StreamDef.


        :param shards: The shards of this StreamDef.  # noqa: E501
        :type: int
        """

        self._shards = shards

    @property
    def ttl_expression(self):
        """Gets the ttl_expression of this StreamDef.  # noqa: E501


        :return: The ttl_expression of this StreamDef.  # noqa: E501
        :rtype: str
        """
        return self._ttl_expression

    @ttl_expression.setter
    def ttl_expression(self, ttl_expression):
        """Sets the ttl_expression of this StreamDef.


        :param ttl_expression: The ttl_expression of this StreamDef.  # noqa: E501
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
        if issubclass(StreamDef, dict):
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
        if not isinstance(other, StreamDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
