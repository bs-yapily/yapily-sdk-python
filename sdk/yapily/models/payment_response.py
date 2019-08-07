# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.128
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.amount import Amount  # noqa: F401,E501
from yapily.models.charge_details import ChargeDetails  # noqa: F401,E501
from yapily.models.payee import Payee  # noqa: F401,E501
from yapily.models.payment_status_details import PaymentStatusDetails  # noqa: F401,E501


class PaymentResponse(object):
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
        'id': 'str',
        'institution_consent_id': 'str',
        'payment_lifecycle_id': 'str',
        'status': 'str',
        'status_details': 'PaymentStatusDetails',
        'reference': 'str',
        'amount': 'float',
        'currency': 'str',
        'amount_details': 'Amount',
        'charge_details': 'list[ChargeDetails]',
        'payee_details': 'Payee',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'institution_consent_id': 'institutionConsentId',
        'payment_lifecycle_id': 'paymentLifecycleId',
        'status': 'status',
        'status_details': 'statusDetails',
        'reference': 'reference',
        'amount': 'amount',
        'currency': 'currency',
        'amount_details': 'amountDetails',
        'charge_details': 'chargeDetails',
        'payee_details': 'payeeDetails',
        'created_at': 'createdAt'
    }

    def __init__(self, id=None, institution_consent_id=None, payment_lifecycle_id=None, status=None, status_details=None, reference=None, amount=None, currency=None, amount_details=None, charge_details=None, payee_details=None, created_at=None):  # noqa: E501
        """PaymentResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._institution_consent_id = None
        self._payment_lifecycle_id = None
        self._status = None
        self._status_details = None
        self._reference = None
        self._amount = None
        self._currency = None
        self._amount_details = None
        self._charge_details = None
        self._payee_details = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if institution_consent_id is not None:
            self.institution_consent_id = institution_consent_id
        if payment_lifecycle_id is not None:
            self.payment_lifecycle_id = payment_lifecycle_id
        if status is not None:
            self.status = status
        if status_details is not None:
            self.status_details = status_details
        if reference is not None:
            self.reference = reference
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if amount_details is not None:
            self.amount_details = amount_details
        if charge_details is not None:
            self.charge_details = charge_details
        if payee_details is not None:
            self.payee_details = payee_details
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this PaymentResponse.  # noqa: E501


        :return: The id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentResponse.


        :param id: The id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def institution_consent_id(self):
        """Gets the institution_consent_id of this PaymentResponse.  # noqa: E501


        :return: The institution_consent_id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._institution_consent_id

    @institution_consent_id.setter
    def institution_consent_id(self, institution_consent_id):
        """Sets the institution_consent_id of this PaymentResponse.


        :param institution_consent_id: The institution_consent_id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._institution_consent_id = institution_consent_id

    @property
    def payment_lifecycle_id(self):
        """Gets the payment_lifecycle_id of this PaymentResponse.  # noqa: E501


        :return: The payment_lifecycle_id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_lifecycle_id

    @payment_lifecycle_id.setter
    def payment_lifecycle_id(self, payment_lifecycle_id):
        """Sets the payment_lifecycle_id of this PaymentResponse.


        :param payment_lifecycle_id: The payment_lifecycle_id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._payment_lifecycle_id = payment_lifecycle_id

    @property
    def status(self):
        """Gets the status of this PaymentResponse.  # noqa: E501


        :return: The status of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentResponse.


        :param status: The status of this PaymentResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "FAILED", "DECLINED", "COMPLETED", "EXPIRED", "UNKNOWN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_details(self):
        """Gets the status_details of this PaymentResponse.  # noqa: E501


        :return: The status_details of this PaymentResponse.  # noqa: E501
        :rtype: PaymentStatusDetails
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """Sets the status_details of this PaymentResponse.


        :param status_details: The status_details of this PaymentResponse.  # noqa: E501
        :type: PaymentStatusDetails
        """

        self._status_details = status_details

    @property
    def reference(self):
        """Gets the reference of this PaymentResponse.  # noqa: E501


        :return: The reference of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PaymentResponse.


        :param reference: The reference of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def amount(self):
        """Gets the amount of this PaymentResponse.  # noqa: E501


        :return: The amount of this PaymentResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentResponse.


        :param amount: The amount of this PaymentResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this PaymentResponse.  # noqa: E501


        :return: The currency of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentResponse.


        :param currency: The currency of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def amount_details(self):
        """Gets the amount_details of this PaymentResponse.  # noqa: E501


        :return: The amount_details of this PaymentResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._amount_details

    @amount_details.setter
    def amount_details(self, amount_details):
        """Sets the amount_details of this PaymentResponse.


        :param amount_details: The amount_details of this PaymentResponse.  # noqa: E501
        :type: Amount
        """

        self._amount_details = amount_details

    @property
    def charge_details(self):
        """Gets the charge_details of this PaymentResponse.  # noqa: E501


        :return: The charge_details of this PaymentResponse.  # noqa: E501
        :rtype: list[ChargeDetails]
        """
        return self._charge_details

    @charge_details.setter
    def charge_details(self, charge_details):
        """Sets the charge_details of this PaymentResponse.


        :param charge_details: The charge_details of this PaymentResponse.  # noqa: E501
        :type: list[ChargeDetails]
        """

        self._charge_details = charge_details

    @property
    def payee_details(self):
        """Gets the payee_details of this PaymentResponse.  # noqa: E501


        :return: The payee_details of this PaymentResponse.  # noqa: E501
        :rtype: Payee
        """
        return self._payee_details

    @payee_details.setter
    def payee_details(self, payee_details):
        """Sets the payee_details of this PaymentResponse.


        :param payee_details: The payee_details of this PaymentResponse.  # noqa: E501
        :type: Payee
        """

        self._payee_details = payee_details

    @property
    def created_at(self):
        """Gets the created_at of this PaymentResponse.  # noqa: E501


        :return: The created_at of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PaymentResponse.


        :param created_at: The created_at of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if not isinstance(other, PaymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
