# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.112
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.other_residency_type import OtherResidencyType  # noqa: F401,E501


class ResidencyEligibility(object):
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
        'notes': 'list[str]',
        'other_residency_type': 'OtherResidencyType',
        'residency_included': 'list[str]',
        'residency_type': 'str'
    }

    attribute_map = {
        'notes': 'Notes',
        'other_residency_type': 'OtherResidencyType',
        'residency_included': 'ResidencyIncluded',
        'residency_type': 'ResidencyType'
    }

    def __init__(self, notes=None, other_residency_type=None, residency_included=None, residency_type=None):  # noqa: E501
        """ResidencyEligibility - a model defined in Swagger"""  # noqa: E501

        self._notes = None
        self._other_residency_type = None
        self._residency_included = None
        self._residency_type = None
        self.discriminator = None

        if notes is not None:
            self.notes = notes
        if other_residency_type is not None:
            self.other_residency_type = other_residency_type
        if residency_included is not None:
            self.residency_included = residency_included
        if residency_type is not None:
            self.residency_type = residency_type

    @property
    def notes(self):
        """Gets the notes of this ResidencyEligibility.  # noqa: E501


        :return: The notes of this ResidencyEligibility.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ResidencyEligibility.


        :param notes: The notes of this ResidencyEligibility.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def other_residency_type(self):
        """Gets the other_residency_type of this ResidencyEligibility.  # noqa: E501


        :return: The other_residency_type of this ResidencyEligibility.  # noqa: E501
        :rtype: OtherResidencyType
        """
        return self._other_residency_type

    @other_residency_type.setter
    def other_residency_type(self, other_residency_type):
        """Sets the other_residency_type of this ResidencyEligibility.


        :param other_residency_type: The other_residency_type of this ResidencyEligibility.  # noqa: E501
        :type: OtherResidencyType
        """

        self._other_residency_type = other_residency_type

    @property
    def residency_included(self):
        """Gets the residency_included of this ResidencyEligibility.  # noqa: E501


        :return: The residency_included of this ResidencyEligibility.  # noqa: E501
        :rtype: list[str]
        """
        return self._residency_included

    @residency_included.setter
    def residency_included(self, residency_included):
        """Sets the residency_included of this ResidencyEligibility.


        :param residency_included: The residency_included of this ResidencyEligibility.  # noqa: E501
        :type: list[str]
        """

        self._residency_included = residency_included

    @property
    def residency_type(self):
        """Gets the residency_type of this ResidencyEligibility.  # noqa: E501


        :return: The residency_type of this ResidencyEligibility.  # noqa: E501
        :rtype: str
        """
        return self._residency_type

    @residency_type.setter
    def residency_type(self, residency_type):
        """Sets the residency_type of this ResidencyEligibility.


        :param residency_type: The residency_type of this ResidencyEligibility.  # noqa: E501
        :type: str
        """
        allowed_values = ["Householder", "Other"]  # noqa: E501
        if residency_type not in allowed_values:
            raise ValueError(
                "Invalid value for `residency_type` ({0}), must be one of {1}"  # noqa: E501
                .format(residency_type, allowed_values)
            )

        self._residency_type = residency_type

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
        if not isinstance(other, ResidencyEligibility):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
