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

class UpdateSourceRequest(object):
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
        'connection_config': 'ConnectionConfig',
        'description': 'str',
        'name': 'str',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'connection_config': 'connection_config',
        'description': 'description',
        'name': 'name',
        'properties': 'properties'
    }

    def __init__(self, connection_config=None, description=None, name=None, properties=None):  # noqa: E501
        """UpdateSourceRequest - a model defined in Swagger"""  # noqa: E501
        self._connection_config = None
        self._description = None
        self._name = None
        self._properties = None
        self.discriminator = None
        if connection_config is not None:
            self.connection_config = connection_config
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties

    @property
    def connection_config(self):
        """Gets the connection_config of this UpdateSourceRequest.  # noqa: E501


        :return: The connection_config of this UpdateSourceRequest.  # noqa: E501
        :rtype: ConnectionConfig
        """
        return self._connection_config

    @connection_config.setter
    def connection_config(self, connection_config):
        """Sets the connection_config of this UpdateSourceRequest.


        :param connection_config: The connection_config of this UpdateSourceRequest.  # noqa: E501
        :type: ConnectionConfig
        """

        self._connection_config = connection_config

    @property
    def description(self):
        """Gets the description of this UpdateSourceRequest.  # noqa: E501


        :return: The description of this UpdateSourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSourceRequest.


        :param description: The description of this UpdateSourceRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this UpdateSourceRequest.  # noqa: E501


        :return: The name of this UpdateSourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSourceRequest.


        :param name: The name of this UpdateSourceRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this UpdateSourceRequest.  # noqa: E501


        :return: The properties of this UpdateSourceRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpdateSourceRequest.


        :param properties: The properties of this UpdateSourceRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

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
        if issubclass(UpdateSourceRequest, dict):
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
        if not isinstance(other, UpdateSourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other