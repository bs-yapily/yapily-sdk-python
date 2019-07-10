# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.124
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yapily.api_client import ApiClient


class PaymentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_payment_authorisation_with_sort_code_using_post(self, payment_auth_request, **kwargs):  # noqa: E501
        """Initiate a new single payment for user to authorise  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_payment_authorisation_with_sort_code_using_post(payment_auth_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param SortCodePaymentAuthRequest payment_auth_request: paymentAuthRequest (required)
        :return: ApiResponseOfAuthorisationRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_payment_authorisation_with_sort_code_using_post_with_http_info(payment_auth_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_payment_authorisation_with_sort_code_using_post_with_http_info(payment_auth_request, **kwargs)  # noqa: E501
            return data

    def create_payment_authorisation_with_sort_code_using_post_with_http_info(self, payment_auth_request, **kwargs):  # noqa: E501
        """Initiate a new single payment for user to authorise  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_payment_authorisation_with_sort_code_using_post_with_http_info(payment_auth_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param SortCodePaymentAuthRequest payment_auth_request: paymentAuthRequest (required)
        :return: ApiResponseOfAuthorisationRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_auth_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_payment_authorisation_with_sort_code_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_auth_request' is set
        if ('payment_auth_request' not in params or
                params['payment_auth_request'] is None):
            raise ValueError("Missing the required parameter `payment_auth_request` when calling `create_payment_authorisation_with_sort_code_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_auth_request' in params:
            body_params = params['payment_auth_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/payment-sortcode-auth-requests', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfAuthorisationRequestResponse',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_payment_with_sort_code_using_post(self, consent, payment_request, **kwargs):  # noqa: E501
        """Create a new single payment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_payment_with_sort_code_using_post(consent, payment_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent: Consent Token (required)
        :param SortCodePaymentRequest payment_request: paymentRequest (required)
        :return: ApiResponseOfPaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_payment_with_sort_code_using_post_with_http_info(consent, payment_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_payment_with_sort_code_using_post_with_http_info(consent, payment_request, **kwargs)  # noqa: E501
            return data

    def create_payment_with_sort_code_using_post_with_http_info(self, consent, payment_request, **kwargs):  # noqa: E501
        """Create a new single payment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_payment_with_sort_code_using_post_with_http_info(consent, payment_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent: Consent Token (required)
        :param SortCodePaymentRequest payment_request: paymentRequest (required)
        :return: ApiResponseOfPaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent', 'payment_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_payment_with_sort_code_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent' is set
        if ('consent' not in params or
                params['consent'] is None):
            raise ValueError("Missing the required parameter `consent` when calling `create_payment_with_sort_code_using_post`")  # noqa: E501
        # verify the required parameter 'payment_request' is set
        if ('payment_request' not in params or
                params['payment_request'] is None):
            raise ValueError("Missing the required parameter `payment_request` when calling `create_payment_with_sort_code_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'consent' in params:
            header_params['consent'] = params['consent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_request' in params:
            body_params = params['payment_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/payment-sortcode', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfPaymentResponse',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payment_status_using_get(self, payment_id, consent, **kwargs):  # noqa: E501
        """Get status of a payment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_payment_status_using_get(payment_id, consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_id: paymentId (required)
        :param str consent: Consent Token (required)
        :return: ApiResponseOfPaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_payment_status_using_get_with_http_info(payment_id, consent, **kwargs)  # noqa: E501
        else:
            (data) = self.get_payment_status_using_get_with_http_info(payment_id, consent, **kwargs)  # noqa: E501
            return data

    def get_payment_status_using_get_with_http_info(self, payment_id, consent, **kwargs):  # noqa: E501
        """Get status of a payment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_payment_status_using_get_with_http_info(payment_id, consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_id: paymentId (required)
        :param str consent: Consent Token (required)
        :return: ApiResponseOfPaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_id', 'consent']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_status_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `get_payment_status_using_get`")  # noqa: E501
        # verify the required parameter 'consent' is set
        if ('consent' not in params or
                params['consent'] is None):
            raise ValueError("Missing the required parameter `consent` when calling `get_payment_status_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_id' in params:
            path_params['paymentId'] = params['payment_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'consent' in params:
            header_params['consent'] = params['consent']  # noqa: E501

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
            '/payments/{paymentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfPaymentResponse',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
