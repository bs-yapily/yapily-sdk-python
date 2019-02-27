# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.87
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.consents_api import ConsentsApi  # noqa: E501
from yapily.rest import ApiException


class TestConsentsApi(unittest.TestCase):
    """ConsentsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.consents_api.ConsentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_consent_using_post(self):
        """Test case for add_consent_using_post

        Post consent  # noqa: E501
        """
        pass

    def test_delete_using_delete(self):
        """Test case for delete_using_delete

        Delete consent  # noqa: E501
        """
        pass

    def test_get_consent_by_id_using_get(self):
        """Test case for get_consent_by_id_using_get

        Get consent  # noqa: E501
        """
        pass

    def test_get_user_consents_using_get(self):
        """Test case for get_user_consents_using_get

        Get user consents  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
