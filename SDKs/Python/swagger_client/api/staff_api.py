# coding: utf-8

"""
    MINDBODY Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class StaffApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def staff_get_staff(self, site_id, version, **kwargs):  # noqa: E501
        """Get staff members at a site.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.staff_get_staff(site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :param list[str] request_filters: Filters to apply to the search. Possible values are:  * StaffViewable  * AppointmentInstructor  * ClassInstructor  * Male  * Female
        :param int request_limit: Number of results to include, defaults to 100
        :param int request_location_id: Return only staff members that are available at the specified location. You must supply a valid `SessionTypeID` and `StartDateTime` to use this parameter.
        :param int request_offset: Page offset, defaults to 0.
        :param int request_session_type_id: Return only staff members that are available for the specified session type. You must supply a valid `StartDateTime` and `LocationID` to use this parameter.
        :param list[int] request_staff_ids: A list of the requested staff IDs.
        :param datetime request_start_date_time: Return only staff members that are available at the specified date and time. You must supply a valid `SessionTypeID` and `LocationID` to use this parameter.
        :return: GetStaffResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.staff_get_staff_with_http_info(site_id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.staff_get_staff_with_http_info(site_id, version, **kwargs)  # noqa: E501
            return data

    def staff_get_staff_with_http_info(self, site_id, version, **kwargs):  # noqa: E501
        """Get staff members at a site.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.staff_get_staff_with_http_info(site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :param list[str] request_filters: Filters to apply to the search. Possible values are:  * StaffViewable  * AppointmentInstructor  * ClassInstructor  * Male  * Female
        :param int request_limit: Number of results to include, defaults to 100
        :param int request_location_id: Return only staff members that are available at the specified location. You must supply a valid `SessionTypeID` and `StartDateTime` to use this parameter.
        :param int request_offset: Page offset, defaults to 0.
        :param int request_session_type_id: Return only staff members that are available for the specified session type. You must supply a valid `StartDateTime` and `LocationID` to use this parameter.
        :param list[int] request_staff_ids: A list of the requested staff IDs.
        :param datetime request_start_date_time: Return only staff members that are available at the specified date and time. You must supply a valid `SessionTypeID` and `LocationID` to use this parameter.
        :return: GetStaffResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'version', 'authorization', 'request_filters', 'request_limit', 'request_location_id', 'request_offset', 'request_session_type_id', 'request_staff_ids', 'request_start_date_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method staff_get_staff" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `staff_get_staff`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `staff_get_staff`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []
        if 'request_filters' in params:
            query_params.append(('request.filters', params['request_filters']))  # noqa: E501
            collection_formats['request.filters'] = 'multi'  # noqa: E501
        if 'request_limit' in params:
            query_params.append(('request.limit', params['request_limit']))  # noqa: E501
        if 'request_location_id' in params:
            query_params.append(('request.locationId', params['request_location_id']))  # noqa: E501
        if 'request_offset' in params:
            query_params.append(('request.offset', params['request_offset']))  # noqa: E501
        if 'request_session_type_id' in params:
            query_params.append(('request.sessionTypeId', params['request_session_type_id']))  # noqa: E501
        if 'request_staff_ids' in params:
            query_params.append(('request.staffIds', params['request_staff_ids']))  # noqa: E501
            collection_formats['request.staffIds'] = 'multi'  # noqa: E501
        if 'request_start_date_time' in params:
            query_params.append(('request.startDateTime', params['request_start_date_time']))  # noqa: E501

        header_params = {}
        if 'site_id' in params:
            header_params['siteId'] = params['site_id']  # noqa: E501
        if 'authorization' in params:
            header_params['authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/public/v{version}/staff/staff', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetStaffResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def staff_get_staff_permissions(self, request_staff_id, site_id, version, **kwargs):  # noqa: E501
        """Get configured staff permissions for a staff member.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.staff_get_staff_permissions(request_staff_id, site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int request_staff_id: The ID of the staff member whose permissions you want to return. (required)
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :return: GetStaffPermissionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.staff_get_staff_permissions_with_http_info(request_staff_id, site_id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.staff_get_staff_permissions_with_http_info(request_staff_id, site_id, version, **kwargs)  # noqa: E501
            return data

    def staff_get_staff_permissions_with_http_info(self, request_staff_id, site_id, version, **kwargs):  # noqa: E501
        """Get configured staff permissions for a staff member.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.staff_get_staff_permissions_with_http_info(request_staff_id, site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int request_staff_id: The ID of the staff member whose permissions you want to return. (required)
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :return: GetStaffPermissionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_staff_id', 'site_id', 'version', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method staff_get_staff_permissions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request_staff_id' is set
        if ('request_staff_id' not in params or
                params['request_staff_id'] is None):
            raise ValueError("Missing the required parameter `request_staff_id` when calling `staff_get_staff_permissions`")  # noqa: E501
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `staff_get_staff_permissions`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `staff_get_staff_permissions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []
        if 'request_staff_id' in params:
            query_params.append(('request.staffId', params['request_staff_id']))  # noqa: E501

        header_params = {}
        if 'site_id' in params:
            header_params['siteId'] = params['site_id']  # noqa: E501
        if 'authorization' in params:
            header_params['authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/public/v{version}/staff/staffpermissions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetStaffPermissionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
