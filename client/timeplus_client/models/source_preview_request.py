# coding: utf-8

"""
    Timeplus

    Welcome to the Timeplus HTTP REST API specification.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: support@timeplus.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SourcePreviewRequest(object):
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
        'properties': 'dict(str, object)',
        'size': 'int',
        'type': 'str'
    }

    attribute_map = {
        'properties': 'properties',
        'size': 'size',
        'type': 'type'
    }

    def __init__(self, properties=None, size=None, type=None):  # noqa: E501
        """SourcePreviewRequest - a model defined in Swagger"""  # noqa: E501
        self._properties = None
        self._size = None
        self._type = None
        self.discriminator = None
        if properties is not None:
            self.properties = properties
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type

    @property
    def properties(self):
        """Gets the properties of this SourcePreviewRequest.  # noqa: E501


        :return: The properties of this SourcePreviewRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SourcePreviewRequest.


        :param properties: The properties of this SourcePreviewRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

    @property
    def size(self):
        """Gets the size of this SourcePreviewRequest.  # noqa: E501


        :return: The size of this SourcePreviewRequest.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SourcePreviewRequest.


        :param size: The size of this SourcePreviewRequest.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def type(self):
        """Gets the type of this SourcePreviewRequest.  # noqa: E501


        :return: The type of this SourcePreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SourcePreviewRequest.


        :param type: The type of this SourcePreviewRequest.  # noqa: E501
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
        if issubclass(SourcePreviewRequest, dict):
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
        if not isinstance(other, SourcePreviewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other