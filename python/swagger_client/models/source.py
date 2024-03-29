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

class Source(object):
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
        'description': 'str',
        'id': 'str',
        'last_updated_at': 'str',
        'last_updated_by': 'Owner',
        'message': 'str',
        'name': 'str',
        'properties': 'dict(str, object)',
        'start_time': 'int',
        'status': 'str',
        'stream': 'str',
        'type': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'created_by': 'created_by',
        'description': 'description',
        'id': 'id',
        'last_updated_at': 'last_updated_at',
        'last_updated_by': 'last_updated_by',
        'message': 'message',
        'name': 'name',
        'properties': 'properties',
        'start_time': 'start_time',
        'status': 'status',
        'stream': 'stream',
        'type': 'type'
    }

    def __init__(self, created_at=None, created_by=None, description=None, id=None, last_updated_at=None, last_updated_by=None, message=None, name=None, properties=None, start_time=None, status=None, stream=None, type=None):  # noqa: E501
        """Source - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._created_by = None
        self._description = None
        self._id = None
        self._last_updated_at = None
        self._last_updated_by = None
        self._message = None
        self._name = None
        self._properties = None
        self._start_time = None
        self._status = None
        self._stream = None
        self._type = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        self.description = description
        self.id = id
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        self.message = message
        self.name = name
        self.properties = properties
        self.start_time = start_time
        self.status = status
        self.stream = stream
        self.type = type

    @property
    def created_at(self):
        """Gets the created_at of this Source.  # noqa: E501


        :return: The created_at of this Source.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Source.


        :param created_at: The created_at of this Source.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Source.  # noqa: E501


        :return: The created_by of this Source.  # noqa: E501
        :rtype: Owner
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Source.


        :param created_by: The created_by of this Source.  # noqa: E501
        :type: Owner
        """

        self._created_by = created_by

    @property
    def description(self):
        """Gets the description of this Source.  # noqa: E501


        :return: The description of this Source.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Source.


        :param description: The description of this Source.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this Source.  # noqa: E501


        :return: The id of this Source.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Source.


        :param id: The id of this Source.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this Source.  # noqa: E501


        :return: The last_updated_at of this Source.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this Source.


        :param last_updated_at: The last_updated_at of this Source.  # noqa: E501
        :type: str
        """

        self._last_updated_at = last_updated_at

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this Source.  # noqa: E501


        :return: The last_updated_by of this Source.  # noqa: E501
        :rtype: Owner
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this Source.


        :param last_updated_by: The last_updated_by of this Source.  # noqa: E501
        :type: Owner
        """

        self._last_updated_by = last_updated_by

    @property
    def message(self):
        """Gets the message of this Source.  # noqa: E501


        :return: The message of this Source.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Source.


        :param message: The message of this Source.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def name(self):
        """Gets the name of this Source.  # noqa: E501


        :return: The name of this Source.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Source.


        :param name: The name of this Source.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this Source.  # noqa: E501

        Additional properties of the source  # noqa: E501

        :return: The properties of this Source.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Source.

        Additional properties of the source  # noqa: E501

        :param properties: The properties of this Source.  # noqa: E501
        :type: dict(str, object)
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def start_time(self):
        """Gets the start_time of this Source.  # noqa: E501

        Unix timestamp when the source get started  # noqa: E501

        :return: The start_time of this Source.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Source.

        Unix timestamp when the source get started  # noqa: E501

        :param start_time: The start_time of this Source.  # noqa: E501
        :type: int
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this Source.  # noqa: E501


        :return: The status of this Source.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Source.


        :param status: The status of this Source.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def stream(self):
        """Gets the stream of this Source.  # noqa: E501

        The name of the target stream that this source writes to.  # noqa: E501

        :return: The stream of this Source.  # noqa: E501
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this Source.

        The name of the target stream that this source writes to.  # noqa: E501

        :param stream: The stream of this Source.  # noqa: E501
        :type: str
        """
        if stream is None:
            raise ValueError("Invalid value for `stream`, must not be `None`")  # noqa: E501

        self._stream = stream

    @property
    def type(self):
        """Gets the type of this Source.  # noqa: E501

        Type of the source  # noqa: E501

        :return: The type of this Source.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Source.

        Type of the source  # noqa: E501

        :param type: The type of this Source.  # noqa: E501
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
        if issubclass(Source, dict):
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
        if not isinstance(other, Source):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
