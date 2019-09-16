# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.142
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class URI(object):
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
        'absolute': 'bool',
        'authority': 'str',
        'fragment': 'str',
        'host': 'str',
        'opaque': 'bool',
        'path': 'str',
        'port': 'int',
        'query': 'str',
        'raw_authority': 'str',
        'raw_fragment': 'str',
        'raw_path': 'str',
        'raw_query': 'str',
        'raw_scheme_specific_part': 'str',
        'raw_user_info': 'str',
        'scheme': 'str',
        'scheme_specific_part': 'str',
        'user_info': 'str'
    }

    attribute_map = {
        'absolute': 'absolute',
        'authority': 'authority',
        'fragment': 'fragment',
        'host': 'host',
        'opaque': 'opaque',
        'path': 'path',
        'port': 'port',
        'query': 'query',
        'raw_authority': 'rawAuthority',
        'raw_fragment': 'rawFragment',
        'raw_path': 'rawPath',
        'raw_query': 'rawQuery',
        'raw_scheme_specific_part': 'rawSchemeSpecificPart',
        'raw_user_info': 'rawUserInfo',
        'scheme': 'scheme',
        'scheme_specific_part': 'schemeSpecificPart',
        'user_info': 'userInfo'
    }

    def __init__(self, absolute=None, authority=None, fragment=None, host=None, opaque=None, path=None, port=None, query=None, raw_authority=None, raw_fragment=None, raw_path=None, raw_query=None, raw_scheme_specific_part=None, raw_user_info=None, scheme=None, scheme_specific_part=None, user_info=None):  # noqa: E501
        """URI - a model defined in Swagger"""  # noqa: E501

        self._absolute = None
        self._authority = None
        self._fragment = None
        self._host = None
        self._opaque = None
        self._path = None
        self._port = None
        self._query = None
        self._raw_authority = None
        self._raw_fragment = None
        self._raw_path = None
        self._raw_query = None
        self._raw_scheme_specific_part = None
        self._raw_user_info = None
        self._scheme = None
        self._scheme_specific_part = None
        self._user_info = None
        self.discriminator = None

        if absolute is not None:
            self.absolute = absolute
        if authority is not None:
            self.authority = authority
        if fragment is not None:
            self.fragment = fragment
        if host is not None:
            self.host = host
        if opaque is not None:
            self.opaque = opaque
        if path is not None:
            self.path = path
        if port is not None:
            self.port = port
        if query is not None:
            self.query = query
        if raw_authority is not None:
            self.raw_authority = raw_authority
        if raw_fragment is not None:
            self.raw_fragment = raw_fragment
        if raw_path is not None:
            self.raw_path = raw_path
        if raw_query is not None:
            self.raw_query = raw_query
        if raw_scheme_specific_part is not None:
            self.raw_scheme_specific_part = raw_scheme_specific_part
        if raw_user_info is not None:
            self.raw_user_info = raw_user_info
        if scheme is not None:
            self.scheme = scheme
        if scheme_specific_part is not None:
            self.scheme_specific_part = scheme_specific_part
        if user_info is not None:
            self.user_info = user_info

    @property
    def absolute(self):
        """Gets the absolute of this URI.  # noqa: E501


        :return: The absolute of this URI.  # noqa: E501
        :rtype: bool
        """
        return self._absolute

    @absolute.setter
    def absolute(self, absolute):
        """Sets the absolute of this URI.


        :param absolute: The absolute of this URI.  # noqa: E501
        :type: bool
        """

        self._absolute = absolute

    @property
    def authority(self):
        """Gets the authority of this URI.  # noqa: E501


        :return: The authority of this URI.  # noqa: E501
        :rtype: str
        """
        return self._authority

    @authority.setter
    def authority(self, authority):
        """Sets the authority of this URI.


        :param authority: The authority of this URI.  # noqa: E501
        :type: str
        """

        self._authority = authority

    @property
    def fragment(self):
        """Gets the fragment of this URI.  # noqa: E501


        :return: The fragment of this URI.  # noqa: E501
        :rtype: str
        """
        return self._fragment

    @fragment.setter
    def fragment(self, fragment):
        """Sets the fragment of this URI.


        :param fragment: The fragment of this URI.  # noqa: E501
        :type: str
        """

        self._fragment = fragment

    @property
    def host(self):
        """Gets the host of this URI.  # noqa: E501


        :return: The host of this URI.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this URI.


        :param host: The host of this URI.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def opaque(self):
        """Gets the opaque of this URI.  # noqa: E501


        :return: The opaque of this URI.  # noqa: E501
        :rtype: bool
        """
        return self._opaque

    @opaque.setter
    def opaque(self, opaque):
        """Sets the opaque of this URI.


        :param opaque: The opaque of this URI.  # noqa: E501
        :type: bool
        """

        self._opaque = opaque

    @property
    def path(self):
        """Gets the path of this URI.  # noqa: E501


        :return: The path of this URI.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this URI.


        :param path: The path of this URI.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def port(self):
        """Gets the port of this URI.  # noqa: E501


        :return: The port of this URI.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this URI.


        :param port: The port of this URI.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def query(self):
        """Gets the query of this URI.  # noqa: E501


        :return: The query of this URI.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this URI.


        :param query: The query of this URI.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def raw_authority(self):
        """Gets the raw_authority of this URI.  # noqa: E501


        :return: The raw_authority of this URI.  # noqa: E501
        :rtype: str
        """
        return self._raw_authority

    @raw_authority.setter
    def raw_authority(self, raw_authority):
        """Sets the raw_authority of this URI.


        :param raw_authority: The raw_authority of this URI.  # noqa: E501
        :type: str
        """

        self._raw_authority = raw_authority

    @property
    def raw_fragment(self):
        """Gets the raw_fragment of this URI.  # noqa: E501


        :return: The raw_fragment of this URI.  # noqa: E501
        :rtype: str
        """
        return self._raw_fragment

    @raw_fragment.setter
    def raw_fragment(self, raw_fragment):
        """Sets the raw_fragment of this URI.


        :param raw_fragment: The raw_fragment of this URI.  # noqa: E501
        :type: str
        """

        self._raw_fragment = raw_fragment

    @property
    def raw_path(self):
        """Gets the raw_path of this URI.  # noqa: E501


        :return: The raw_path of this URI.  # noqa: E501
        :rtype: str
        """
        return self._raw_path

    @raw_path.setter
    def raw_path(self, raw_path):
        """Sets the raw_path of this URI.


        :param raw_path: The raw_path of this URI.  # noqa: E501
        :type: str
        """

        self._raw_path = raw_path

    @property
    def raw_query(self):
        """Gets the raw_query of this URI.  # noqa: E501


        :return: The raw_query of this URI.  # noqa: E501
        :rtype: str
        """
        return self._raw_query

    @raw_query.setter
    def raw_query(self, raw_query):
        """Sets the raw_query of this URI.


        :param raw_query: The raw_query of this URI.  # noqa: E501
        :type: str
        """

        self._raw_query = raw_query

    @property
    def raw_scheme_specific_part(self):
        """Gets the raw_scheme_specific_part of this URI.  # noqa: E501


        :return: The raw_scheme_specific_part of this URI.  # noqa: E501
        :rtype: str
        """
        return self._raw_scheme_specific_part

    @raw_scheme_specific_part.setter
    def raw_scheme_specific_part(self, raw_scheme_specific_part):
        """Sets the raw_scheme_specific_part of this URI.


        :param raw_scheme_specific_part: The raw_scheme_specific_part of this URI.  # noqa: E501
        :type: str
        """

        self._raw_scheme_specific_part = raw_scheme_specific_part

    @property
    def raw_user_info(self):
        """Gets the raw_user_info of this URI.  # noqa: E501


        :return: The raw_user_info of this URI.  # noqa: E501
        :rtype: str
        """
        return self._raw_user_info

    @raw_user_info.setter
    def raw_user_info(self, raw_user_info):
        """Sets the raw_user_info of this URI.


        :param raw_user_info: The raw_user_info of this URI.  # noqa: E501
        :type: str
        """

        self._raw_user_info = raw_user_info

    @property
    def scheme(self):
        """Gets the scheme of this URI.  # noqa: E501


        :return: The scheme of this URI.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this URI.


        :param scheme: The scheme of this URI.  # noqa: E501
        :type: str
        """

        self._scheme = scheme

    @property
    def scheme_specific_part(self):
        """Gets the scheme_specific_part of this URI.  # noqa: E501


        :return: The scheme_specific_part of this URI.  # noqa: E501
        :rtype: str
        """
        return self._scheme_specific_part

    @scheme_specific_part.setter
    def scheme_specific_part(self, scheme_specific_part):
        """Sets the scheme_specific_part of this URI.


        :param scheme_specific_part: The scheme_specific_part of this URI.  # noqa: E501
        :type: str
        """

        self._scheme_specific_part = scheme_specific_part

    @property
    def user_info(self):
        """Gets the user_info of this URI.  # noqa: E501


        :return: The user_info of this URI.  # noqa: E501
        :rtype: str
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        """Sets the user_info of this URI.


        :param user_info: The user_info of this URI.  # noqa: E501
        :type: str
        """

        self._user_info = user_info

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
        if not isinstance(other, URI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
