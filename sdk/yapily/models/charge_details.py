# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.115
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.amount import Amount  # noqa: F401,E501


class ChargeDetails(object):
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
        'charge_amount': 'Amount'
    }

    attribute_map = {
        'charge_amount': 'chargeAmount'
    }

    def __init__(self, charge_amount=None):  # noqa: E501
        """ChargeDetails - a model defined in Swagger"""  # noqa: E501

        self._charge_amount = None
        self.discriminator = None

        if charge_amount is not None:
            self.charge_amount = charge_amount

    @property
    def charge_amount(self):
        """Gets the charge_amount of this ChargeDetails.  # noqa: E501

        Amount paid by charge bearer  # noqa: E501

        :return: The charge_amount of this ChargeDetails.  # noqa: E501
        :rtype: Amount
        """
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, charge_amount):
        """Sets the charge_amount of this ChargeDetails.

        Amount paid by charge bearer  # noqa: E501

        :param charge_amount: The charge_amount of this ChargeDetails.  # noqa: E501
        :type: Amount
        """

        self._charge_amount = charge_amount

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChargeDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
