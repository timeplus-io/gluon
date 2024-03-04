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

class Stream(object):
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
        'columns': 'list[ColumnsResp]',
        'created_at': 'str',
        'created_by': 'Owner',
        'description': 'str',
        'engine': 'str',
        'is_external': 'bool',
        'last_updated_at': 'str',
        'last_updated_by': 'Owner',
        'logstore_retention_bytes': 'int',
        'logstore_retention_ms': 'int',
        'mode': 'str',
        'name': 'str',
        'primary_key': 'str',
        'ttl': 'str',
        'ttl_expression': 'str'
    }

    attribute_map = {
        'columns': 'columns',
        'created_at': 'created_at',
        'created_by': 'created_by',
        'description': 'description',
        'engine': 'engine',
        'is_external': 'is_external',
        'last_updated_at': 'last_updated_at',
        'last_updated_by': 'last_updated_by',
        'logstore_retention_bytes': 'logstore_retention_bytes',
        'logstore_retention_ms': 'logstore_retention_ms',
        'mode': 'mode',
        'name': 'name',
        'primary_key': 'primary_key',
        'ttl': 'ttl',
        'ttl_expression': 'ttl_expression'
    }

    def __init__(self, columns=None, created_at=None, created_by=None, description=None, engine=None, is_external=None, last_updated_at=None, last_updated_by=None, logstore_retention_bytes=None, logstore_retention_ms=None, mode=None, name=None, primary_key=None, ttl=None, ttl_expression=None):  # noqa: E501
        """Stream - a model defined in Swagger"""  # noqa: E501
        self._columns = None
        self._created_at = None
        self._created_by = None
        self._description = None
        self._engine = None
        self._is_external = None
        self._last_updated_at = None
        self._last_updated_by = None
        self._logstore_retention_bytes = None
        self._logstore_retention_ms = None
        self._mode = None
        self._name = None
        self._primary_key = None
        self._ttl = None
        self._ttl_expression = None
        self.discriminator = None
        self.columns = columns
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        self.description = description
        self.engine = engine
        if is_external is not None:
            self.is_external = is_external
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        self.logstore_retention_bytes = logstore_retention_bytes
        self.logstore_retention_ms = logstore_retention_ms
        self.mode = mode
        self.name = name
        if primary_key is not None:
            self.primary_key = primary_key
        self.ttl = ttl
        self.ttl_expression = ttl_expression

    @property
    def columns(self):
        """Gets the columns of this Stream.  # noqa: E501


        :return: The columns of this Stream.  # noqa: E501
        :rtype: list[ColumnsResp]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this Stream.


        :param columns: The columns of this Stream.  # noqa: E501
        :type: list[ColumnsResp]
        """
        if columns is None:
            raise ValueError("Invalid value for `columns`, must not be `None`")  # noqa: E501

        self._columns = columns

    @property
    def created_at(self):
        """Gets the created_at of this Stream.  # noqa: E501


        :return: The created_at of this Stream.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Stream.


        :param created_at: The created_at of this Stream.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Stream.  # noqa: E501


        :return: The created_by of this Stream.  # noqa: E501
        :rtype: Owner
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Stream.


        :param created_by: The created_by of this Stream.  # noqa: E501
        :type: Owner
        """

        self._created_by = created_by

    @property
    def description(self):
        """Gets the description of this Stream.  # noqa: E501


        :return: The description of this Stream.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Stream.


        :param description: The description of this Stream.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def engine(self):
        """Gets the engine of this Stream.  # noqa: E501


        :return: The engine of this Stream.  # noqa: E501
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this Stream.


        :param engine: The engine of this Stream.  # noqa: E501
        :type: str
        """
        if engine is None:
            raise ValueError("Invalid value for `engine`, must not be `None`")  # noqa: E501

        self._engine = engine

    @property
    def is_external(self):
        """Gets the is_external of this Stream.  # noqa: E501

        Deprecated.  # noqa: E501

        :return: The is_external of this Stream.  # noqa: E501
        :rtype: bool
        """
        return self._is_external

    @is_external.setter
    def is_external(self, is_external):
        """Sets the is_external of this Stream.

        Deprecated.  # noqa: E501

        :param is_external: The is_external of this Stream.  # noqa: E501
        :type: bool
        """

        self._is_external = is_external

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this Stream.  # noqa: E501


        :return: The last_updated_at of this Stream.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this Stream.


        :param last_updated_at: The last_updated_at of this Stream.  # noqa: E501
        :type: str
        """

        self._last_updated_at = last_updated_at

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this Stream.  # noqa: E501


        :return: The last_updated_by of this Stream.  # noqa: E501
        :rtype: Owner
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this Stream.


        :param last_updated_by: The last_updated_by of this Stream.  # noqa: E501
        :type: Owner
        """

        self._last_updated_by = last_updated_by

    @property
    def logstore_retention_bytes(self):
        """Gets the logstore_retention_bytes of this Stream.  # noqa: E501

        The max size a stream can grow. Any non-positive value means unlimited size.  # noqa: E501

        :return: The logstore_retention_bytes of this Stream.  # noqa: E501
        :rtype: int
        """
        return self._logstore_retention_bytes

    @logstore_retention_bytes.setter
    def logstore_retention_bytes(self, logstore_retention_bytes):
        """Sets the logstore_retention_bytes of this Stream.

        The max size a stream can grow. Any non-positive value means unlimited size.  # noqa: E501

        :param logstore_retention_bytes: The logstore_retention_bytes of this Stream.  # noqa: E501
        :type: int
        """
        if logstore_retention_bytes is None:
            raise ValueError("Invalid value for `logstore_retention_bytes`, must not be `None`")  # noqa: E501

        self._logstore_retention_bytes = logstore_retention_bytes

    @property
    def logstore_retention_ms(self):
        """Gets the logstore_retention_ms of this Stream.  # noqa: E501

        The max time the data can be retained in the stream. Any non-positive value means unlimited time.  # noqa: E501

        :return: The logstore_retention_ms of this Stream.  # noqa: E501
        :rtype: int
        """
        return self._logstore_retention_ms

    @logstore_retention_ms.setter
    def logstore_retention_ms(self, logstore_retention_ms):
        """Sets the logstore_retention_ms of this Stream.

        The max time the data can be retained in the stream. Any non-positive value means unlimited time.  # noqa: E501

        :param logstore_retention_ms: The logstore_retention_ms of this Stream.  # noqa: E501
        :type: int
        """
        if logstore_retention_ms is None:
            raise ValueError("Invalid value for `logstore_retention_ms`, must not be `None`")  # noqa: E501

        self._logstore_retention_ms = logstore_retention_ms

    @property
    def mode(self):
        """Gets the mode of this Stream.  # noqa: E501

        Storage mode of stream. Defaulted to `append`.  # noqa: E501

        :return: The mode of this Stream.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Stream.

        Storage mode of stream. Defaulted to `append`.  # noqa: E501

        :param mode: The mode of this Stream.  # noqa: E501
        :type: str
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        allowed_values = ["append", "changelog", "changelog_kv", "versioned_kv"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def name(self):
        """Gets the name of this Stream.  # noqa: E501


        :return: The name of this Stream.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Stream.


        :param name: The name of this Stream.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def primary_key(self):
        """Gets the primary_key of this Stream.  # noqa: E501

        Expression of primary key, required in `changelog_kv` and `versioned_kv` mode  # noqa: E501

        :return: The primary_key of this Stream.  # noqa: E501
        :rtype: str
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """Sets the primary_key of this Stream.

        Expression of primary key, required in `changelog_kv` and `versioned_kv` mode  # noqa: E501

        :param primary_key: The primary_key of this Stream.  # noqa: E501
        :type: str
        """

        self._primary_key = primary_key

    @property
    def ttl(self):
        """Gets the ttl of this Stream.  # noqa: E501

        Deprecated. Use `ttl_expression` instaed  # noqa: E501

        :return: The ttl of this Stream.  # noqa: E501
        :rtype: str
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this Stream.

        Deprecated. Use `ttl_expression` instaed  # noqa: E501

        :param ttl: The ttl of this Stream.  # noqa: E501
        :type: str
        """
        if ttl is None:
            raise ValueError("Invalid value for `ttl`, must not be `None`")  # noqa: E501

        self._ttl = ttl

    @property
    def ttl_expression(self):
        """Gets the ttl_expression of this Stream.  # noqa: E501

        ORDER_BY     string        `json:\"order_by_expression\"` PATTITION_BY string        `json:\"partition_by_expression\"`  # noqa: E501

        :return: The ttl_expression of this Stream.  # noqa: E501
        :rtype: str
        """
        return self._ttl_expression

    @ttl_expression.setter
    def ttl_expression(self, ttl_expression):
        """Sets the ttl_expression of this Stream.

        ORDER_BY     string        `json:\"order_by_expression\"` PATTITION_BY string        `json:\"partition_by_expression\"`  # noqa: E501

        :param ttl_expression: The ttl_expression of this Stream.  # noqa: E501
        :type: str
        """
        if ttl_expression is None:
            raise ValueError("Invalid value for `ttl_expression`, must not be `None`")  # noqa: E501

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
        if issubclass(Stream, dict):
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
        if not isinstance(other, Stream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
