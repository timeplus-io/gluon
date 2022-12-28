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

class CreateDashboardRequest(object):
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
        'panels': 'list[DashboardPanel]'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'panels': 'panels'
    }

    def __init__(self, description=None, name=None, panels=None):  # noqa: E501
        """CreateDashboardRequest - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._name = None
        self._panels = None
        self.discriminator = None
        if description is not None:
            self.description = description
        self.name = name
        if panels is not None:
            self.panels = panels

    @property
    def description(self):
        """Gets the description of this CreateDashboardRequest.  # noqa: E501


        :return: The description of this CreateDashboardRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDashboardRequest.


        :param description: The description of this CreateDashboardRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateDashboardRequest.  # noqa: E501


        :return: The name of this CreateDashboardRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDashboardRequest.


        :param name: The name of this CreateDashboardRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def panels(self):
        """Gets the panels of this CreateDashboardRequest.  # noqa: E501


        :return: The panels of this CreateDashboardRequest.  # noqa: E501
        :rtype: list[DashboardPanel]
        """
        return self._panels

    @panels.setter
    def panels(self, panels):
        """Sets the panels of this CreateDashboardRequest.


        :param panels: The panels of this CreateDashboardRequest.  # noqa: E501
        :type: list[DashboardPanel]
        """

        self._panels = panels

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
        if issubclass(CreateDashboardRequest, dict):
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
        if not isinstance(other, CreateDashboardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
