# coding: utf-8

"""
    Timeplus

    Welcome to the Timeplus HTTP REST API specification.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@timeplus.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SinksV1beta2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1beta2_sinks_get(self, **kwargs):  # noqa: E501
        """list sinks  # noqa: E501

        Get all sinks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Sink]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_sinks_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_sinks_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1beta2_sinks_get_with_http_info(self, **kwargs):  # noqa: E501
        """list sinks  # noqa: E501

        Get all sinks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Sink]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_sinks_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/sinks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Sink]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_sinks_id_delete(self, id, **kwargs):  # noqa: E501
        """delete a sink  # noqa: E501

        Delete a sink with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: sink ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_sinks_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_sinks_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1beta2_sinks_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """delete a sink  # noqa: E501

        Delete a sink with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: sink ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_sinks_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1beta2_sinks_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/sinks/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_sinks_id_get(self, id, **kwargs):  # noqa: E501
        """get a sink  # noqa: E501

        Get a sink with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: sink ID (required)
        :return: Sink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_sinks_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_sinks_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1beta2_sinks_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """get a sink  # noqa: E501

        Get a sink with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: sink ID (required)
        :return: Sink
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_sinks_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1beta2_sinks_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/sinks/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Sink',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_sinks_id_put(self, body, id, **kwargs):  # noqa: E501
        """update a sink  # noqa: E501

        Update the specific sink with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_put(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateSinkRequest body: update sink request parameters (required)
        :param str id: sink ID (required)
        :return: Sink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_sinks_id_put_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_sinks_id_put_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def v1beta2_sinks_id_put_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """update a sink  # noqa: E501

        Update the specific sink with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_put_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateSinkRequest body: update sink request parameters (required)
        :param str id: sink ID (required)
        :return: Sink
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_sinks_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1beta2_sinks_id_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1beta2_sinks_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/sinks/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Sink',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_sinks_id_start_post(self, id, **kwargs):  # noqa: E501
        """start a sink  # noqa: E501

        Start the sink with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_start_post(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: sink ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_sinks_id_start_post_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_sinks_id_start_post_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1beta2_sinks_id_start_post_with_http_info(self, id, **kwargs):  # noqa: E501
        """start a sink  # noqa: E501

        Start the sink with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_start_post_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: sink ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_sinks_id_start_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1beta2_sinks_id_start_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/sinks/{id}/start', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_sinks_id_stats_get(self, id, error_log_time_range, metrics_time_range, **kwargs):  # noqa: E501
        """get the stats of a sink  # noqa: E501

        Get the stats of a sink with the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_stats_get(id, error_log_time_range, metrics_time_range, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: sink ID (required)
        :param str error_log_time_range: (required)
        :param str metrics_time_range: (required)
        :return: SinkStats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_sinks_id_stats_get_with_http_info(id, error_log_time_range, metrics_time_range, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_sinks_id_stats_get_with_http_info(id, error_log_time_range, metrics_time_range, **kwargs)  # noqa: E501
            return data

    def v1beta2_sinks_id_stats_get_with_http_info(self, id, error_log_time_range, metrics_time_range, **kwargs):  # noqa: E501
        """get the stats of a sink  # noqa: E501

        Get the stats of a sink with the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_stats_get_with_http_info(id, error_log_time_range, metrics_time_range, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: sink ID (required)
        :param str error_log_time_range: (required)
        :param str metrics_time_range: (required)
        :return: SinkStats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'error_log_time_range', 'metrics_time_range']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_sinks_id_stats_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1beta2_sinks_id_stats_get`")  # noqa: E501
        # verify the required parameter 'error_log_time_range' is set
        if ('error_log_time_range' not in params or
                params['error_log_time_range'] is None):
            raise ValueError("Missing the required parameter `error_log_time_range` when calling `v1beta2_sinks_id_stats_get`")  # noqa: E501
        # verify the required parameter 'metrics_time_range' is set
        if ('metrics_time_range' not in params or
                params['metrics_time_range'] is None):
            raise ValueError("Missing the required parameter `metrics_time_range` when calling `v1beta2_sinks_id_stats_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'error_log_time_range' in params:
            query_params.append(('error_log_time_range', params['error_log_time_range']))  # noqa: E501
        if 'metrics_time_range' in params:
            query_params.append(('metrics_time_range', params['metrics_time_range']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/sinks/{id}/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SinkStats',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_sinks_id_stop_post(self, id, **kwargs):  # noqa: E501
        """stop a sink  # noqa: E501

        Stop the sink with the given ID from sending out data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_stop_post(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: sink ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_sinks_id_stop_post_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_sinks_id_stop_post_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1beta2_sinks_id_stop_post_with_http_info(self, id, **kwargs):  # noqa: E501
        """stop a sink  # noqa: E501

        Stop the sink with the given ID from sending out data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_id_stop_post_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: sink ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_sinks_id_stop_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1beta2_sinks_id_stop_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/sinks/{id}/stop', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_sinks_post(self, body, **kwargs):  # noqa: E501
        """create a sink  # noqa: E501

        Create a sink. Please refer to the documentation of [sink](https://docs.timeplus.com/destination) for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateSinkRequest body: create sink request parameters (required)
        :return: Sink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_sinks_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_sinks_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1beta2_sinks_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """create a sink  # noqa: E501

        Create a sink. Please refer to the documentation of [sink](https://docs.timeplus.com/destination) for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sinks_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateSinkRequest body: create sink request parameters (required)
        :return: Sink
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_sinks_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1beta2_sinks_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/sinks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Sink',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
