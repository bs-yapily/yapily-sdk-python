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


class AccountStatement(object):
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
        'start_date_time': 'datetime',
        'end_date_time': 'datetime',
        'creation_date_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'start_date_time': 'startDateTime',
        'end_date_time': 'endDateTime',
        'creation_date_time': 'creationDateTime'
    }

    def __init__(self, id=None, start_date_time=None, end_date_time=None, creation_date_time=None):  # noqa: E501
        """AccountStatement - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._start_date_time = None
        self._end_date_time = None
        self._creation_date_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if start_date_time is not None:
            self.start_date_time = start_date_time
        if end_date_time is not None:
            self.end_date_time = end_date_time
        if creation_date_time is not None:
            self.creation_date_time = creation_date_time

    @property
    def id(self):
        """Gets the id of this AccountStatement.  # noqa: E501


        :return: The id of this AccountStatement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountStatement.


        :param id: The id of this AccountStatement.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def start_date_time(self):
        """Gets the start_date_time of this AccountStatement.  # noqa: E501


        :return: The start_date_time of this AccountStatement.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this AccountStatement.


        :param start_date_time: The start_date_time of this AccountStatement.  # noqa: E501
        :type: datetime
        """

        self._start_date_time = start_date_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this AccountStatement.  # noqa: E501


        :return: The end_date_time of this AccountStatement.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this AccountStatement.


        :param end_date_time: The end_date_time of this AccountStatement.  # noqa: E501
        :type: datetime
        """

        self._end_date_time = end_date_time

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this AccountStatement.  # noqa: E501


        :return: The creation_date_time of this AccountStatement.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this AccountStatement.


        :param creation_date_time: The creation_date_time of this AccountStatement.  # noqa: E501
        :type: datetime
        """

        self._creation_date_time = creation_date_time

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
        if not isinstance(other, AccountStatement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
