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

class CreateAlertRequest(object):
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
        'action': 'str',
        'description': 'str',
        'name': 'str',
        'properties': 'dict(str, object)',
        'resolve_sql': 'str',
        'severity': 'int',
        'trigger_sql': 'str'
    }

    attribute_map = {
        'action': 'action',
        'description': 'description',
        'name': 'name',
        'properties': 'properties',
        'resolve_sql': 'resolve_sql',
        'severity': 'severity',
        'trigger_sql': 'trigger_sql'
    }

    def __init__(self, action=None, description=None, name=None, properties=None, resolve_sql=None, severity=None, trigger_sql=None):  # noqa: E501
        """CreateAlertRequest - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._description = None
        self._name = None
        self._properties = None
        self._resolve_sql = None
        self._severity = None
        self._trigger_sql = None
        self.discriminator = None
        self.action = action
        if description is not None:
            self.description = description
        self.name = name
        if properties is not None:
            self.properties = properties
        if resolve_sql is not None:
            self.resolve_sql = resolve_sql
        self.severity = severity
        self.trigger_sql = trigger_sql

    @property
    def action(self):
        """Gets the action of this CreateAlertRequest.  # noqa: E501

        Sink template - the following properties are used to create the sink One action can be map to a sink  # noqa: E501

        :return: The action of this CreateAlertRequest.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateAlertRequest.

        Sink template - the following properties are used to create the sink One action can be map to a sink  # noqa: E501

        :param action: The action of this CreateAlertRequest.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def description(self):
        """Gets the description of this CreateAlertRequest.  # noqa: E501


        :return: The description of this CreateAlertRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAlertRequest.


        :param description: The description of this CreateAlertRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateAlertRequest.  # noqa: E501


        :return: The name of this CreateAlertRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAlertRequest.


        :param name: The name of this CreateAlertRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this CreateAlertRequest.  # noqa: E501

        Detailed properties to create the sink  # noqa: E501

        :return: The properties of this CreateAlertRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CreateAlertRequest.

        Detailed properties to create the sink  # noqa: E501

        :param properties: The properties of this CreateAlertRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

    @property
    def resolve_sql(self):
        """Gets the resolve_sql of this CreateAlertRequest.  # noqa: E501


        :return: The resolve_sql of this CreateAlertRequest.  # noqa: E501
        :rtype: str
        """
        return self._resolve_sql

    @resolve_sql.setter
    def resolve_sql(self, resolve_sql):
        """Sets the resolve_sql of this CreateAlertRequest.


        :param resolve_sql: The resolve_sql of this CreateAlertRequest.  # noqa: E501
        :type: str
        """

        self._resolve_sql = resolve_sql

    @property
    def severity(self):
        """Gets the severity of this CreateAlertRequest.  # noqa: E501


        :return: The severity of this CreateAlertRequest.  # noqa: E501
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this CreateAlertRequest.


        :param severity: The severity of this CreateAlertRequest.  # noqa: E501
        :type: int
        """
        if severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501

        self._severity = severity

    @property
    def trigger_sql(self):
        """Gets the trigger_sql of this CreateAlertRequest.  # noqa: E501

        Persistent query template - the following properties are used to create the persistent query  # noqa: E501

        :return: The trigger_sql of this CreateAlertRequest.  # noqa: E501
        :rtype: str
        """
        return self._trigger_sql

    @trigger_sql.setter
    def trigger_sql(self, trigger_sql):
        """Sets the trigger_sql of this CreateAlertRequest.

        Persistent query template - the following properties are used to create the persistent query  # noqa: E501

        :param trigger_sql: The trigger_sql of this CreateAlertRequest.  # noqa: E501
        :type: str
        """
        if trigger_sql is None:
            raise ValueError("Invalid value for `trigger_sql`, must not be `None`")  # noqa: E501

        self._trigger_sql = trigger_sql

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
        if issubclass(CreateAlertRequest, dict):
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
        if not isinstance(other, CreateAlertRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
