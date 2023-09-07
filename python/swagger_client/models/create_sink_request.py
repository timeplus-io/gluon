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

class CreateSinkRequest(object):
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
        'description': 'str',
        'name': 'str',
        'properties': 'dict(str, object)',
        'query': 'str',
        'sql': 'str',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'properties': 'properties',
        'query': 'query',
        'sql': 'sql',
        'type': 'type'
    }

    def __init__(self, description=None, name=None, properties=None, query=None, sql=None, type=None):  # noqa: E501
        """CreateSinkRequest - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._name = None
        self._properties = None
        self._query = None
        self._sql = None
        self._type = None
        self.discriminator = None
        if description is not None:
            self.description = description
        self.name = name
        if properties is not None:
            self.properties = properties
        if query is not None:
            self.query = query
        if sql is not None:
            self.sql = sql
        self.type = type

    @property
    def description(self):
        """Gets the description of this CreateSinkRequest.  # noqa: E501


        :return: The description of this CreateSinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSinkRequest.


        :param description: The description of this CreateSinkRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateSinkRequest.  # noqa: E501

        Sink name should only contain a maximum of 64 letters, numbers, or _, and start with a letter  # noqa: E501

        :return: The name of this CreateSinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSinkRequest.

        Sink name should only contain a maximum of 64 letters, numbers, or _, and start with a letter  # noqa: E501

        :param name: The name of this CreateSinkRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this CreateSinkRequest.  # noqa: E501

        Additional properties that required to write the data to the sink (e.g. broker url). Please refer to the documentation for this sink type  # noqa: E501

        :return: The properties of this CreateSinkRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CreateSinkRequest.

        Additional properties that required to write the data to the sink (e.g. broker url). Please refer to the documentation for this sink type  # noqa: E501

        :param properties: The properties of this CreateSinkRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

    @property
    def query(self):
        """Gets the query of this CreateSinkRequest.  # noqa: E501


        :return: The query of this CreateSinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this CreateSinkRequest.


        :param query: The query of this CreateSinkRequest.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def sql(self):
        """Gets the sql of this CreateSinkRequest.  # noqa: E501

        Deprecated. Use `query` instead.  # noqa: E501

        :return: The sql of this CreateSinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this CreateSinkRequest.

        Deprecated. Use `query` instead.  # noqa: E501

        :param sql: The sql of this CreateSinkRequest.  # noqa: E501
        :type: str
        """

        self._sql = sql

    @property
    def type(self):
        """Gets the type of this CreateSinkRequest.  # noqa: E501

        Available types: [`slack`, `http`, `kafka`, `redpanda`, `confluent_cloud`, `pulsar`, `timeplus`]. Additional configurations such as broker url and etc. should be passed through `properties`  # noqa: E501

        :return: The type of this CreateSinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateSinkRequest.

        Available types: [`slack`, `http`, `kafka`, `redpanda`, `confluent_cloud`, `pulsar`, `timeplus`]. Additional configurations such as broker url and etc. should be passed through `properties`  # noqa: E501

        :param type: The type of this CreateSinkRequest.  # noqa: E501
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
        if issubclass(CreateSinkRequest, dict):
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
        if not isinstance(other, CreateSinkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
