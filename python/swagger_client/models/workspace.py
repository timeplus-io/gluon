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

class Workspace(object):
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
        'created_at': 'str',
        'created_by': 'Owner',
        'demo_mode': 'bool',
        'enabled_subscription': 'bool',
        'free_trial_end_date': 'str',
        'id': 'str',
        'last_updated_at': 'str',
        'last_updated_by': 'Owner',
        'name': 'str',
        'settings': 'WorkspaceSettings'
    }

    attribute_map = {
        'created_at': 'created_at',
        'created_by': 'created_by',
        'demo_mode': 'demo_mode',
        'enabled_subscription': 'enabled_subscription',
        'free_trial_end_date': 'free_trial_end_date',
        'id': 'id',
        'last_updated_at': 'last_updated_at',
        'last_updated_by': 'last_updated_by',
        'name': 'name',
        'settings': 'settings'
    }

    def __init__(self, created_at=None, created_by=None, demo_mode=None, enabled_subscription=None, free_trial_end_date=None, id=None, last_updated_at=None, last_updated_by=None, name=None, settings=None):  # noqa: E501
        """Workspace - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._created_by = None
        self._demo_mode = None
        self._enabled_subscription = None
        self._free_trial_end_date = None
        self._id = None
        self._last_updated_at = None
        self._last_updated_by = None
        self._name = None
        self._settings = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        self.demo_mode = demo_mode
        self.enabled_subscription = enabled_subscription
        if free_trial_end_date is not None:
            self.free_trial_end_date = free_trial_end_date
        self.id = id
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        self.name = name
        self.settings = settings

    @property
    def created_at(self):
        """Gets the created_at of this Workspace.  # noqa: E501


        :return: The created_at of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Workspace.


        :param created_at: The created_at of this Workspace.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Workspace.  # noqa: E501


        :return: The created_by of this Workspace.  # noqa: E501
        :rtype: Owner
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Workspace.


        :param created_by: The created_by of this Workspace.  # noqa: E501
        :type: Owner
        """

        self._created_by = created_by

    @property
    def demo_mode(self):
        """Gets the demo_mode of this Workspace.  # noqa: E501

        Whether this is a demo worksapce  # noqa: E501

        :return: The demo_mode of this Workspace.  # noqa: E501
        :rtype: bool
        """
        return self._demo_mode

    @demo_mode.setter
    def demo_mode(self, demo_mode):
        """Sets the demo_mode of this Workspace.

        Whether this is a demo worksapce  # noqa: E501

        :param demo_mode: The demo_mode of this Workspace.  # noqa: E501
        :type: bool
        """
        if demo_mode is None:
            raise ValueError("Invalid value for `demo_mode`, must not be `None`")  # noqa: E501

        self._demo_mode = demo_mode

    @property
    def enabled_subscription(self):
        """Gets the enabled_subscription of this Workspace.  # noqa: E501

        Whether subscription feature is enabled for this workspace  # noqa: E501

        :return: The enabled_subscription of this Workspace.  # noqa: E501
        :rtype: bool
        """
        return self._enabled_subscription

    @enabled_subscription.setter
    def enabled_subscription(self, enabled_subscription):
        """Sets the enabled_subscription of this Workspace.

        Whether subscription feature is enabled for this workspace  # noqa: E501

        :param enabled_subscription: The enabled_subscription of this Workspace.  # noqa: E501
        :type: bool
        """
        if enabled_subscription is None:
            raise ValueError("Invalid value for `enabled_subscription`, must not be `None`")  # noqa: E501

        self._enabled_subscription = enabled_subscription

    @property
    def free_trial_end_date(self):
        """Gets the free_trial_end_date of this Workspace.  # noqa: E501

        When Free Trial ends, if applicable  # noqa: E501

        :return: The free_trial_end_date of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._free_trial_end_date

    @free_trial_end_date.setter
    def free_trial_end_date(self, free_trial_end_date):
        """Sets the free_trial_end_date of this Workspace.

        When Free Trial ends, if applicable  # noqa: E501

        :param free_trial_end_date: The free_trial_end_date of this Workspace.  # noqa: E501
        :type: str
        """

        self._free_trial_end_date = free_trial_end_date

    @property
    def id(self):
        """Gets the id of this Workspace.  # noqa: E501


        :return: The id of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Workspace.


        :param id: The id of this Workspace.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this Workspace.  # noqa: E501


        :return: The last_updated_at of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this Workspace.


        :param last_updated_at: The last_updated_at of this Workspace.  # noqa: E501
        :type: str
        """

        self._last_updated_at = last_updated_at

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this Workspace.  # noqa: E501


        :return: The last_updated_by of this Workspace.  # noqa: E501
        :rtype: Owner
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this Workspace.


        :param last_updated_by: The last_updated_by of this Workspace.  # noqa: E501
        :type: Owner
        """

        self._last_updated_by = last_updated_by

    @property
    def name(self):
        """Gets the name of this Workspace.  # noqa: E501

        Friendly name of the workspace  # noqa: E501

        :return: The name of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Workspace.

        Friendly name of the workspace  # noqa: E501

        :param name: The name of this Workspace.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def settings(self):
        """Gets the settings of this Workspace.  # noqa: E501


        :return: The settings of this Workspace.  # noqa: E501
        :rtype: WorkspaceSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Workspace.


        :param settings: The settings of this Workspace.  # noqa: E501
        :type: WorkspaceSettings
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")  # noqa: E501

        self._settings = settings

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
        if issubclass(Workspace, dict):
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
        if not isinstance(other, Workspace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
