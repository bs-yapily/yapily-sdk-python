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

from yapily.models.personal_current_account_pca import PersonalCurrentAccountPCA  # noqa: F401,E501


class PersonalCurrentAccountBrand(object):
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
        'brand_name': 'str',
        'pca': 'list[PersonalCurrentAccountPCA]'
    }

    attribute_map = {
        'brand_name': 'BrandName',
        'pca': 'PCA'
    }

    def __init__(self, brand_name=None, pca=None):  # noqa: E501
        """PersonalCurrentAccountBrand - a model defined in Swagger"""  # noqa: E501

        self._brand_name = None
        self._pca = None
        self.discriminator = None

        if brand_name is not None:
            self.brand_name = brand_name
        if pca is not None:
            self.pca = pca

    @property
    def brand_name(self):
        """Gets the brand_name of this PersonalCurrentAccountBrand.  # noqa: E501


        :return: The brand_name of this PersonalCurrentAccountBrand.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this PersonalCurrentAccountBrand.


        :param brand_name: The brand_name of this PersonalCurrentAccountBrand.  # noqa: E501
        :type: str
        """

        self._brand_name = brand_name

    @property
    def pca(self):
        """Gets the pca of this PersonalCurrentAccountBrand.  # noqa: E501


        :return: The pca of this PersonalCurrentAccountBrand.  # noqa: E501
        :rtype: list[PersonalCurrentAccountPCA]
        """
        return self._pca

    @pca.setter
    def pca(self, pca):
        """Sets the pca of this PersonalCurrentAccountBrand.


        :param pca: The pca of this PersonalCurrentAccountBrand.  # noqa: E501
        :type: list[PersonalCurrentAccountPCA]
        """

        self._pca = pca

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
        if not isinstance(other, PersonalCurrentAccountBrand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
