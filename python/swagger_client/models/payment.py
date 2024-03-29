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

class Payment(object):
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
        'created': 'int',
        'status': 'str',
        'types': 'list[str]'
    }

    attribute_map = {
        'created': 'created',
        'status': 'status',
        'types': 'types'
    }

    def __init__(self, created=None, status=None, types=None):  # noqa: E501
        """Payment - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._status = None
        self._types = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if status is not None:
            self.status = status
        if types is not None:
            self.types = types

    @property
    def created(self):
        """Gets the created of this Payment.  # noqa: E501


        :return: The created of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Payment.


        :param created: The created of this Payment.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def status(self):
        """Gets the status of this Payment.  # noqa: E501


        :return: The status of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Payment.


        :param status: The status of this Payment.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def types(self):
        """Gets the types of this Payment.  # noqa: E501


        :return: The types of this Payment.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this Payment.


        :param types: The types of this Payment.  # noqa: E501
        :type: list[str]
        """

        self._types = types

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
        if issubclass(Payment, dict):
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
        if not isinstance(other, Payment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
