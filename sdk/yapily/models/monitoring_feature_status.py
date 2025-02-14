# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.155
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MonitoringFeatureStatus(object):
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
        'last_tested': 'datetime',
        'span': 'str',
        'status': 'str'
    }

    attribute_map = {
        'last_tested': 'lastTested',
        'span': 'span',
        'status': 'status'
    }

    def __init__(self, last_tested=None, span=None, status=None):  # noqa: E501
        """MonitoringFeatureStatus - a model defined in Swagger"""  # noqa: E501

        self._last_tested = None
        self._span = None
        self._status = None
        self.discriminator = None

        if last_tested is not None:
            self.last_tested = last_tested
        if span is not None:
            self.span = span
        if status is not None:
            self.status = status

    @property
    def last_tested(self):
        """Gets the last_tested of this MonitoringFeatureStatus.  # noqa: E501


        :return: The last_tested of this MonitoringFeatureStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_tested

    @last_tested.setter
    def last_tested(self, last_tested):
        """Sets the last_tested of this MonitoringFeatureStatus.


        :param last_tested: The last_tested of this MonitoringFeatureStatus.  # noqa: E501
        :type: datetime
        """

        self._last_tested = last_tested

    @property
    def span(self):
        """Gets the span of this MonitoringFeatureStatus.  # noqa: E501


        :return: The span of this MonitoringFeatureStatus.  # noqa: E501
        :rtype: str
        """
        return self._span

    @span.setter
    def span(self, span):
        """Sets the span of this MonitoringFeatureStatus.


        :param span: The span of this MonitoringFeatureStatus.  # noqa: E501
        :type: str
        """

        self._span = span

    @property
    def status(self):
        """Gets the status of this MonitoringFeatureStatus.  # noqa: E501


        :return: The status of this MonitoringFeatureStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MonitoringFeatureStatus.


        :param status: The status of this MonitoringFeatureStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["Up", "Down", "Warning", "Unknown", "Expired"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, MonitoringFeatureStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
