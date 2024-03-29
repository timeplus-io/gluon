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

class Subscription(object):
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
        'cpu': 'int',
        'customer': 'Customer',
        'payment': 'Payment',
        'storage_size': 'int',
        'subscription_plan': 'str'
    }

    attribute_map = {
        'cpu': 'cpu',
        'customer': 'customer',
        'payment': 'payment',
        'storage_size': 'storage_size',
        'subscription_plan': 'subscription_plan'
    }

    def __init__(self, cpu=None, customer=None, payment=None, storage_size=None, subscription_plan=None):  # noqa: E501
        """Subscription - a model defined in Swagger"""  # noqa: E501
        self._cpu = None
        self._customer = None
        self._payment = None
        self._storage_size = None
        self._subscription_plan = None
        self.discriminator = None
        if cpu is not None:
            self.cpu = cpu
        if customer is not None:
            self.customer = customer
        if payment is not None:
            self.payment = payment
        self.storage_size = storage_size
        self.subscription_plan = subscription_plan

    @property
    def cpu(self):
        """Gets the cpu of this Subscription.  # noqa: E501

        Number of milli CPUs this subscription can use at most (1 CPU == 1000 millicpu), nil means the limit is not set  # noqa: E501

        :return: The cpu of this Subscription.  # noqa: E501
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this Subscription.

        Number of milli CPUs this subscription can use at most (1 CPU == 1000 millicpu), nil means the limit is not set  # noqa: E501

        :param cpu: The cpu of this Subscription.  # noqa: E501
        :type: int
        """

        self._cpu = cpu

    @property
    def customer(self):
        """Gets the customer of this Subscription.  # noqa: E501


        :return: The customer of this Subscription.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Subscription.


        :param customer: The customer of this Subscription.  # noqa: E501
        :type: Customer
        """

        self._customer = customer

    @property
    def payment(self):
        """Gets the payment of this Subscription.  # noqa: E501


        :return: The payment of this Subscription.  # noqa: E501
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this Subscription.


        :param payment: The payment of this Subscription.  # noqa: E501
        :type: Payment
        """

        self._payment = payment

    @property
    def storage_size(self):
        """Gets the storage_size of this Subscription.  # noqa: E501

        Size (in bytes) of the data volume  # noqa: E501

        :return: The storage_size of this Subscription.  # noqa: E501
        :rtype: int
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        """Sets the storage_size of this Subscription.

        Size (in bytes) of the data volume  # noqa: E501

        :param storage_size: The storage_size of this Subscription.  # noqa: E501
        :type: int
        """
        if storage_size is None:
            raise ValueError("Invalid value for `storage_size`, must not be `None`")  # noqa: E501

        self._storage_size = storage_size

    @property
    def subscription_plan(self):
        """Gets the subscription_plan of this Subscription.  # noqa: E501


        :return: The subscription_plan of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._subscription_plan

    @subscription_plan.setter
    def subscription_plan(self, subscription_plan):
        """Sets the subscription_plan of this Subscription.


        :param subscription_plan: The subscription_plan of this Subscription.  # noqa: E501
        :type: str
        """
        if subscription_plan is None:
            raise ValueError("Invalid value for `subscription_plan`, must not be `None`")  # noqa: E501
        allowed_values = ["Free Trial", "Professional", "Enterprise"]  # noqa: E501
        if subscription_plan not in allowed_values:
            raise ValueError(
                "Invalid value for `subscription_plan` ({0}), must be one of {1}"  # noqa: E501
                .format(subscription_plan, allowed_values)
            )

        self._subscription_plan = subscription_plan

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
        if issubclass(Subscription, dict):
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
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
