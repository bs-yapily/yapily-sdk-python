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

from yapily.models.consent_delete_response import ConsentDeleteResponse  # noqa: F401,E501


class UserDeleteResponse(object):
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
        'delete_status': 'str',
        'creation_date': 'datetime',
        'user_consents': 'list[ConsentDeleteResponse]'
    }

    attribute_map = {
        'id': 'id',
        'delete_status': 'deleteStatus',
        'creation_date': 'creationDate',
        'user_consents': 'userConsents'
    }

    def __init__(self, id=None, delete_status=None, creation_date=None, user_consents=None):  # noqa: E501
        """UserDeleteResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._delete_status = None
        self._creation_date = None
        self._user_consents = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if delete_status is not None:
            self.delete_status = delete_status
        if creation_date is not None:
            self.creation_date = creation_date
        if user_consents is not None:
            self.user_consents = user_consents

    @property
    def id(self):
        """Gets the id of this UserDeleteResponse.  # noqa: E501


        :return: The id of this UserDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDeleteResponse.


        :param id: The id of this UserDeleteResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def delete_status(self):
        """Gets the delete_status of this UserDeleteResponse.  # noqa: E501


        :return: The delete_status of this UserDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._delete_status

    @delete_status.setter
    def delete_status(self, delete_status):
        """Sets the delete_status of this UserDeleteResponse.


        :param delete_status: The delete_status of this UserDeleteResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILED"]  # noqa: E501
        if delete_status not in allowed_values:
            raise ValueError(
                "Invalid value for `delete_status` ({0}), must be one of {1}"  # noqa: E501
                .format(delete_status, allowed_values)
            )

        self._delete_status = delete_status

    @property
    def creation_date(self):
        """Gets the creation_date of this UserDeleteResponse.  # noqa: E501


        :return: The creation_date of this UserDeleteResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this UserDeleteResponse.


        :param creation_date: The creation_date of this UserDeleteResponse.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def user_consents(self):
        """Gets the user_consents of this UserDeleteResponse.  # noqa: E501


        :return: The user_consents of this UserDeleteResponse.  # noqa: E501
        :rtype: list[ConsentDeleteResponse]
        """
        return self._user_consents

    @user_consents.setter
    def user_consents(self, user_consents):
        """Sets the user_consents of this UserDeleteResponse.


        :param user_consents: The user_consents of this UserDeleteResponse.  # noqa: E501
        :type: list[ConsentDeleteResponse]
        """

        self._user_consents = user_consents

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
        if not isinstance(other, UserDeleteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
