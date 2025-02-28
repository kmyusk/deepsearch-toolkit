# coding: utf-8

"""
    Corpus Processing Service (CPS) API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsearch.cps.apis.public.api_client import ApiClient
from deepsearch.cps.apis.public.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AnnotateApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def generate_project_object_annotations(self, proj_key, options, **kwargs):  # noqa: E501
        """generate_project_object_annotations  # noqa: E501

        Run an annotator on an object, using resources from the project. *DEPRECATED*, please use generate_project_object_annotations_async instead.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_project_object_annotations(proj_key, options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param AnnotateObjectOptions options: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AnnotatedObject1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.generate_project_object_annotations_with_http_info(proj_key, options, **kwargs)  # noqa: E501

    def generate_project_object_annotations_with_http_info(self, proj_key, options, **kwargs):  # noqa: E501
        """generate_project_object_annotations  # noqa: E501

        Run an annotator on an object, using resources from the project. *DEPRECATED*, please use generate_project_object_annotations_async instead.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_project_object_annotations_with_http_info(proj_key, options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param AnnotateObjectOptions options: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AnnotatedObject1, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'options'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_project_object_annotations" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `generate_project_object_annotations`")  # noqa: E501
        # verify the required parameter 'options' is set
        if self.api_client.client_side_validation and ('options' not in local_var_params or  # noqa: E501
                                                        local_var_params['options'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `options` when calling `generate_project_object_annotations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'options' in local_var_params:
            body_params = local_var_params['options']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/object_annotations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotatedObject1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def generate_project_object_annotations_async(self, proj_key, options, **kwargs):  # noqa: E501
        """generate_project_object_annotations_async  # noqa: E501

        Run an annotator on an object, using resources from the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_project_object_annotations_async(proj_key, options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param AnnotateObjectOptions1 options: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.generate_project_object_annotations_async_with_http_info(proj_key, options, **kwargs)  # noqa: E501

    def generate_project_object_annotations_async_with_http_info(self, proj_key, options, **kwargs):  # noqa: E501
        """generate_project_object_annotations_async  # noqa: E501

        Run an annotator on an object, using resources from the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_project_object_annotations_async_with_http_info(proj_key, options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param AnnotateObjectOptions1 options: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Task, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'options'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_project_object_annotations_async" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `generate_project_object_annotations_async`")  # noqa: E501
        # verify the required parameter 'options' is set
        if self.api_client.client_side_validation and ('options' not in local_var_params or  # noqa: E501
                                                        local_var_params['options'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `options` when calling `generate_project_object_annotations_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'options' in local_var_params:
            body_params = local_var_params['options']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/object_annotations_async', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Task',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cached_annotator_metadata(self, proj_key, options, **kwargs):  # noqa: E501
        """get_cached_annotator_metadata  # noqa: E501

        Get annotator's metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cached_annotator_metadata(proj_key, options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param object options: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AnnotatorMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_cached_annotator_metadata_with_http_info(proj_key, options, **kwargs)  # noqa: E501

    def get_cached_annotator_metadata_with_http_info(self, proj_key, options, **kwargs):  # noqa: E501
        """get_cached_annotator_metadata  # noqa: E501

        Get annotator's metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cached_annotator_metadata_with_http_info(proj_key, options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param object options: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AnnotatorMetadata, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'options'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cached_annotator_metadata" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `get_cached_annotator_metadata`")  # noqa: E501
        # verify the required parameter 'options' is set
        if self.api_client.client_side_validation and ('options' not in local_var_params or  # noqa: E501
                                                        local_var_params['options'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `options` when calling `get_cached_annotator_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'options' in local_var_params:
            body_params = local_var_params['options']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/annotator/metadata', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotatorMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_annotator_supported_annotations(self, proj_key, options, **kwargs):  # noqa: E501
        """get_project_annotator_supported_annotations  # noqa: E501

        Get supported annotations for an annotator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_annotator_supported_annotations(proj_key, options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param object options: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SupportedAnnotatorAnnotations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_project_annotator_supported_annotations_with_http_info(proj_key, options, **kwargs)  # noqa: E501

    def get_project_annotator_supported_annotations_with_http_info(self, proj_key, options, **kwargs):  # noqa: E501
        """get_project_annotator_supported_annotations  # noqa: E501

        Get supported annotations for an annotator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_annotator_supported_annotations_with_http_info(proj_key, options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param object options: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SupportedAnnotatorAnnotations, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'options'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_annotator_supported_annotations" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `get_project_annotator_supported_annotations`")  # noqa: E501
        # verify the required parameter 'options' is set
        if self.api_client.client_side_validation and ('options' not in local_var_params or  # noqa: E501
                                                        local_var_params['options'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `options` when calling `get_project_annotator_supported_annotations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'options' in local_var_params:
            body_params = local_var_params['options']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/annotate/supported_annotations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SupportedAnnotatorAnnotations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_project_inspection_report(self, proj_key, **kwargs):  # noqa: E501
        """list_project_inspection_report  # noqa: E501

        Get paginated list of inspection reports for a project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_project_inspection_report(proj_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param int page: page of the result list
        :param int items_per_page: items on one page of the result list
        :param str search_string: search keyword
        :param int begin_date: begin date of the search date interval
        :param int end_date: end date of the search date interval
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[InspectionReport]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_project_inspection_report_with_http_info(proj_key, **kwargs)  # noqa: E501

    def list_project_inspection_report_with_http_info(self, proj_key, **kwargs):  # noqa: E501
        """list_project_inspection_report  # noqa: E501

        Get paginated list of inspection reports for a project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_project_inspection_report_with_http_info(proj_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param int page: page of the result list
        :param int items_per_page: items on one page of the result list
        :param str search_string: search keyword
        :param int begin_date: begin date of the search date interval
        :param int end_date: end date of the search date interval
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[InspectionReport], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'page',
            'items_per_page',
            'search_string',
            'begin_date',
            'end_date'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_project_inspection_report" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `list_project_inspection_report`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'items_per_page' in local_var_params and local_var_params['items_per_page'] is not None:  # noqa: E501
            query_params.append(('items_per_page', local_var_params['items_per_page']))  # noqa: E501
        if 'search_string' in local_var_params and local_var_params['search_string'] is not None:  # noqa: E501
            query_params.append(('search_string', local_var_params['search_string']))  # noqa: E501
        if 'begin_date' in local_var_params and local_var_params['begin_date'] is not None:  # noqa: E501
            query_params.append(('begin_date', local_var_params['begin_date']))  # noqa: E501
        if 'end_date' in local_var_params and local_var_params['end_date'] is not None:  # noqa: E501
            query_params.append(('end_date', local_var_params['end_date']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/annotate/inspection_report', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InspectionReport]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
