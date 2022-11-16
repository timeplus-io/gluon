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

class CreateQueryRequestV1Beta1(object):
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
        'sql': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'sql': 'sql',
        'tags': 'tags'
    }

    def __init__(self, description=None, name=None, sql=None, tags=None):  # noqa: E501
        """CreateQueryRequestV1Beta1 - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._name = None
        self._sql = None
        self._tags = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if sql is not None:
            self.sql = sql
        if tags is not None:
            self.tags = tags

    @property
    def description(self):
        """Gets the description of this CreateQueryRequestV1Beta1.  # noqa: E501


        :return: The description of this CreateQueryRequestV1Beta1.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateQueryRequestV1Beta1.


        :param description: The description of this CreateQueryRequestV1Beta1.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateQueryRequestV1Beta1.  # noqa: E501


        :return: The name of this CreateQueryRequestV1Beta1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateQueryRequestV1Beta1.


        :param name: The name of this CreateQueryRequestV1Beta1.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sql(self):
        """Gets the sql of this CreateQueryRequestV1Beta1.  # noqa: E501


        :return: The sql of this CreateQueryRequestV1Beta1.  # noqa: E501
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this CreateQueryRequestV1Beta1.


        :param sql: The sql of this CreateQueryRequestV1Beta1.  # noqa: E501
        :type: str
        """

        self._sql = sql

    @property
    def tags(self):
        """Gets the tags of this CreateQueryRequestV1Beta1.  # noqa: E501


        :return: The tags of this CreateQueryRequestV1Beta1.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateQueryRequestV1Beta1.


        :param tags: The tags of this CreateQueryRequestV1Beta1.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if issubclass(CreateQueryRequestV1Beta1, dict):
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
        if not isinstance(other, CreateQueryRequestV1Beta1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other