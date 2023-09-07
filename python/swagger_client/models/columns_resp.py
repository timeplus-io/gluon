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

class ColumnsResp(object):
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
        'nullable': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'codec': 'codec',
        'default': 'default',
        'name': 'name',
        'nullable': 'nullable',
        'type': 'type'
    }

    def __init__(self, codec=None, default=None, name=None, nullable=None, type=None):  # noqa: E501
        """ColumnsResp - a model defined in Swagger"""  # noqa: E501
        self._codec = None
        self._default = None
        self._name = None
        self._nullable = None
        self._type = None
        self.discriminator = None
        if codec is not None:
            self.codec = codec
        if default is not None:
            self.default = default
        if name is not None:
            self.name = name
        if nullable is not None:
            self.nullable = nullable
        if type is not None:
            self.type = type

    @property
    def codec(self):
        """Gets the codec of this ColumnsResp.  # noqa: E501


        :return: The codec of this ColumnsResp.  # noqa: E501
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this ColumnsResp.


        :param codec: The codec of this ColumnsResp.  # noqa: E501
        :type: str
        """

        self._codec = codec

    @property
    def default(self):
        """Gets the default of this ColumnsResp.  # noqa: E501


        :return: The default of this ColumnsResp.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this ColumnsResp.


        :param default: The default of this ColumnsResp.  # noqa: E501
        :type: str
        """

        self._default = default

    @property
    def name(self):
        """Gets the name of this ColumnsResp.  # noqa: E501


        :return: The name of this ColumnsResp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ColumnsResp.


        :param name: The name of this ColumnsResp.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nullable(self):
        """Gets the nullable of this ColumnsResp.  # noqa: E501


        :return: The nullable of this ColumnsResp.  # noqa: E501
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        """Sets the nullable of this ColumnsResp.


        :param nullable: The nullable of this ColumnsResp.  # noqa: E501
        :type: bool
        """

        self._nullable = nullable

    @property
    def type(self):
        """Gets the type of this ColumnsResp.  # noqa: E501


        :return: The type of this ColumnsResp.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ColumnsResp.


        :param type: The type of this ColumnsResp.  # noqa: E501
        :type: str
        """

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
        if issubclass(ColumnsResp, dict):
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
        if not isinstance(other, ColumnsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
