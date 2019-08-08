# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.130
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yapily.api_client import ApiClient


class InstitutionsOpenDataApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_atm_data_using_get(self, institution_id, **kwargs):  # noqa: E501
        """Retrieves data about all ATMs of the selected institution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_atm_data_using_get(institution_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str institution_id: institutionId (required)
        :return: ApiResponseOfListOfATMOpenDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_atm_data_using_get_with_http_info(institution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_atm_data_using_get_with_http_info(institution_id, **kwargs)  # noqa: E501
            return data

    def get_atm_data_using_get_with_http_info(self, institution_id, **kwargs):  # noqa: E501
        """Retrieves data about all ATMs of the selected institution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_atm_data_using_get_with_http_info(institution_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str institution_id: institutionId (required)
        :return: ApiResponseOfListOfATMOpenDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['institution_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_atm_data_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'institution_id' is set
        if ('institution_id' not in params or
                params['institution_id'] is None):
            raise ValueError("Missing the required parameter `institution_id` when calling `get_atm_data_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'institution_id' in params:
            path_params['institutionId'] = params['institution_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/institutions/{institutionId}/atms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfListOfATMOpenDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_personal_current_accounts_using_get(self, institution_id, **kwargs):  # noqa: E501
        """Retrieves details of personal current accounts for an institution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_personal_current_accounts_using_get(institution_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str institution_id: institutionId (required)
        :return: ApiResponseOfListOfPersonalCurrentAccountData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_personal_current_accounts_using_get_with_http_info(institution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_personal_current_accounts_using_get_with_http_info(institution_id, **kwargs)  # noqa: E501
            return data

    def get_personal_current_accounts_using_get_with_http_info(self, institution_id, **kwargs):  # noqa: E501
        """Retrieves details of personal current accounts for an institution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_personal_current_accounts_using_get_with_http_info(institution_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str institution_id: institutionId (required)
        :return: ApiResponseOfListOfPersonalCurrentAccountData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['institution_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_personal_current_accounts_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'institution_id' is set
        if ('institution_id' not in params or
                params['institution_id'] is None):
            raise ValueError("Missing the required parameter `institution_id` when calling `get_personal_current_accounts_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'institution_id' in params:
            path_params['institutionId'] = params['institution_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/institutions/{institutionId}/personal-current-accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfListOfPersonalCurrentAccountData',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
