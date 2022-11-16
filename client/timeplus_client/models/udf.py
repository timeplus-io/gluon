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

class UDF(object):
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
        'arguments': 'list[UDFArgument]',
        'auth_context': 'UDFAuthContext',
        'auth_method': 'str',
        'created_at': 'str',
        'created_by': 'Owner',
        'last_updated_at': 'str',
        'last_updated_by': 'Owner',
        'name': 'str',
        'return_type': 'str',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'arguments': 'arguments',
        'auth_context': 'auth_context',
        'auth_method': 'auth_method',
        'created_at': 'created_at',
        'created_by': 'created_by',
        'last_updated_at': 'last_updated_at',
        'last_updated_by': 'last_updated_by',
        'name': 'name',
        'return_type': 'return_type',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, arguments=None, auth_context=None, auth_method=None, created_at=None, created_by=None, last_updated_at=None, last_updated_by=None, name=None, return_type=None, type=None, url=None):  # noqa: E501
        """UDF - a model defined in Swagger"""  # noqa: E501
        self._arguments = None
        self._auth_context = None
        self._auth_method = None
        self._created_at = None
        self._created_by = None
        self._last_updated_at = None
        self._last_updated_by = None
        self._name = None
        self._return_type = None
        self._type = None
        self._url = None
        self.discriminator = None
        if arguments is not None:
            self.arguments = arguments
        if auth_context is not None:
            self.auth_context = auth_context
        if auth_method is not None:
            self.auth_method = auth_method
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if name is not None:
            self.name = name
        if return_type is not None:
            self.return_type = return_type
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def arguments(self):
        """Gets the arguments of this UDF.  # noqa: E501


        :return: The arguments of this UDF.  # noqa: E501
        :rtype: list[UDFArgument]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this UDF.


        :param arguments: The arguments of this UDF.  # noqa: E501
        :type: list[UDFArgument]
        """

        self._arguments = arguments

    @property
    def auth_context(self):
        """Gets the auth_context of this UDF.  # noqa: E501


        :return: The auth_context of this UDF.  # noqa: E501
        :rtype: UDFAuthContext
        """
        return self._auth_context

    @auth_context.setter
    def auth_context(self, auth_context):
        """Sets the auth_context of this UDF.


        :param auth_context: The auth_context of this UDF.  # noqa: E501
        :type: UDFAuthContext
        """

        self._auth_context = auth_context

    @property
    def auth_method(self):
        """Gets the auth_method of this UDF.  # noqa: E501


        :return: The auth_method of this UDF.  # noqa: E501
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this UDF.


        :param auth_method: The auth_method of this UDF.  # noqa: E501
        :type: str
        """

        self._auth_method = auth_method

    @property
    def created_at(self):
        """Gets the created_at of this UDF.  # noqa: E501


        :return: The created_at of this UDF.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UDF.


        :param created_at: The created_at of this UDF.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this UDF.  # noqa: E501


        :return: The created_by of this UDF.  # noqa: E501
        :rtype: Owner
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UDF.


        :param created_by: The created_by of this UDF.  # noqa: E501
        :type: Owner
        """

        self._created_by = created_by

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this UDF.  # noqa: E501


        :return: The last_updated_at of this UDF.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this UDF.


        :param last_updated_at: The last_updated_at of this UDF.  # noqa: E501
        :type: str
        """

        self._last_updated_at = last_updated_at

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this UDF.  # noqa: E501


        :return: The last_updated_by of this UDF.  # noqa: E501
        :rtype: Owner
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this UDF.


        :param last_updated_by: The last_updated_by of this UDF.  # noqa: E501
        :type: Owner
        """

        self._last_updated_by = last_updated_by

    @property
    def name(self):
        """Gets the name of this UDF.  # noqa: E501


        :return: The name of this UDF.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UDF.


        :param name: The name of this UDF.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def return_type(self):
        """Gets the return_type of this UDF.  # noqa: E501


        :return: The return_type of this UDF.  # noqa: E501
        :rtype: str
        """
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        """Sets the return_type of this UDF.


        :param return_type: The return_type of this UDF.  # noqa: E501
        :type: str
        """

        self._return_type = return_type

    @property
    def type(self):
        """Gets the type of this UDF.  # noqa: E501


        :return: The type of this UDF.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UDF.


        :param type: The type of this UDF.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this UDF.  # noqa: E501


        :return: The url of this UDF.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UDF.


        :param url: The url of this UDF.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(UDF, dict):
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
        if not isinstance(other, UDF):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other