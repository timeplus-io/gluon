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

class ColumnDef(object):
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
        'codec': 'str',
        'default': 'str',
        'name': 'str',
        'skipping_index_expression': 'str',
        'ttl_expression': 'str',
        'type': 'str'
    }

    attribute_map = {
        'codec': 'codec',
        'default': 'default',
        'name': 'name',
        'skipping_index_expression': 'skipping_index_expression',
        'ttl_expression': 'ttl_expression',
        'type': 'type'
    }

    def __init__(self, codec=None, default=None, name=None, skipping_index_expression=None, ttl_expression=None, type=None):  # noqa: E501
        """ColumnDef - a model defined in Swagger"""  # noqa: E501
        self._codec = None
        self._default = None
        self._name = None
        self._skipping_index_expression = None
        self._ttl_expression = None
        self._type = None
        self.discriminator = None
        if codec is not None:
            self.codec = codec
        if default is not None:
            self.default = default
        self.name = name
        if skipping_index_expression is not None:
            self.skipping_index_expression = skipping_index_expression
        if ttl_expression is not None:
            self.ttl_expression = ttl_expression
        self.type = type

    @property
    def codec(self):
        """Gets the codec of this ColumnDef.  # noqa: E501


        :return: The codec of this ColumnDef.  # noqa: E501
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this ColumnDef.


        :param codec: The codec of this ColumnDef.  # noqa: E501
        :type: str
        """

        self._codec = codec

    @property
    def default(self):
        """Gets the default of this ColumnDef.  # noqa: E501


        :return: The default of this ColumnDef.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this ColumnDef.


        :param default: The default of this ColumnDef.  # noqa: E501
        :type: str
        """

        self._default = default

    @property
    def name(self):
        """Gets the name of this ColumnDef.  # noqa: E501


        :return: The name of this ColumnDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ColumnDef.


        :param name: The name of this ColumnDef.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def skipping_index_expression(self):
        """Gets the skipping_index_expression of this ColumnDef.  # noqa: E501


        :return: The skipping_index_expression of this ColumnDef.  # noqa: E501
        :rtype: str
        """
        return self._skipping_index_expression

    @skipping_index_expression.setter
    def skipping_index_expression(self, skipping_index_expression):
        """Sets the skipping_index_expression of this ColumnDef.


        :param skipping_index_expression: The skipping_index_expression of this ColumnDef.  # noqa: E501
        :type: str
        """

        self._skipping_index_expression = skipping_index_expression

    @property
    def ttl_expression(self):
        """Gets the ttl_expression of this ColumnDef.  # noqa: E501


        :return: The ttl_expression of this ColumnDef.  # noqa: E501
        :rtype: str
        """
        return self._ttl_expression

    @ttl_expression.setter
    def ttl_expression(self, ttl_expression):
        """Sets the ttl_expression of this ColumnDef.


        :param ttl_expression: The ttl_expression of this ColumnDef.  # noqa: E501
        :type: str
        """

        self._ttl_expression = ttl_expression

    @property
    def type(self):
        """Gets the type of this ColumnDef.  # noqa: E501


        :return: The type of this ColumnDef.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ColumnDef.


        :param type: The type of this ColumnDef.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(ColumnDef, dict):
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
        if not isinstance(other, ColumnDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
