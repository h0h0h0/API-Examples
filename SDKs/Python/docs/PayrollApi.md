# swagger_client.PayrollApi

All URIs are relative to *https://api.mindbodyonline.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payroll_get_class_payroll**](PayrollApi.md#payroll_get_class_payroll) | **GET** /public/v{version}/payroll/classes | Get class payroll for staff members.
[**payroll_get_time_clock**](PayrollApi.md#payroll_get_time_clock) | **GET** /public/v{version}/payroll/timeclock | Get time card payroll for staff members.


# **payroll_get_class_payroll**
> GetClassPayrollResponse payroll_get_class_payroll(site_id, version, authorization=authorization, request_end_date_time=request_end_date_time, request_include_inactive_staff=request_include_inactive_staff, request_limit=request_limit, request_offset=request_offset, request_staff_id=request_staff_id, request_start_date_time=request_start_date_time)

Get class payroll for staff members.

A staff authorization token is not required for this endpoint, but if one is passed, its permissions are honored. Depending on the access permissions configured for the staff member whose token is passed, the endpoint returns either only the payroll information for that staff member or it returns the payroll information for all staff members.    Note that if a staff member is not paid for a class, earnings of zero are returned by this endpoint.    Note that this endpoint calculates both bonus and no-reg rates for assistants.These rates are not supported by the Payroll report in the web interface.    Note that this endpoint returns both the teacher’s adjusted rate and the assistant’s pay rate when the assistant is paid by the teacher.The Payroll report in the web interface only returns the teacher’s adjusted rate.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PayrollApi()
site_id = 'site_id_example' # str | ID of the site from which to pull data.
version = 'version_example' # str | 
authorization = '' # str | A staff user authorization token. (optional) (default to )
request_end_date_time = '2013-10-20T19:20:30+01:00' # datetime | The end of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br />  Default: **Today’s date**  * If you do not supply an `EndDateTime`, the data returns for the period from the `StartDateTime` that you supply to today’s date.  * If you do not supply an `EndDateTime` or a `StartDateTime`, data returns for the seven days prior to today’s date. (optional)
request_include_inactive_staff = true # bool | When `true`, payroll information returns for both active and inactive staff members.<br />  Default: **false** (optional)
request_limit = 56 # int | Number of results to include, defaults to 100 (optional)
request_offset = 56 # int | Page offset, defaults to 0. (optional)
request_staff_id = 789 # int | A list of staff IDs that you want to retrieve payroll information for. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID. (optional)
request_start_date_time = '2013-10-20T19:20:30+01:00' # datetime | The beginning of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.  * If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply.  * If you do not supply either a `StartDateTime` or an `EndDateTime`, the data returns for seven days prior to today’s date. (optional)

try:
    # Get class payroll for staff members.
    api_response = api_instance.payroll_get_class_payroll(site_id, version, authorization=authorization, request_end_date_time=request_end_date_time, request_include_inactive_staff=request_include_inactive_staff, request_limit=request_limit, request_offset=request_offset, request_staff_id=request_staff_id, request_start_date_time=request_start_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollApi->payroll_get_class_payroll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| ID of the site from which to pull data. | 
 **version** | **str**|  | 
 **authorization** | **str**| A staff user authorization token. | [optional] [default to ]
 **request_end_date_time** | **datetime**| The end of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.&lt;br /&gt;  Default: **Today’s date**  * If you do not supply an &#x60;EndDateTime&#x60;, the data returns for the period from the &#x60;StartDateTime&#x60; that you supply to today’s date.  * If you do not supply an &#x60;EndDateTime&#x60; or a &#x60;StartDateTime&#x60;, data returns for the seven days prior to today’s date. | [optional] 
 **request_include_inactive_staff** | **bool**| When &#x60;true&#x60;, payroll information returns for both active and inactive staff members.&lt;br /&gt;  Default: **false** | [optional] 
 **request_limit** | **int**| Number of results to include, defaults to 100 | [optional] 
 **request_offset** | **int**| Page offset, defaults to 0. | [optional] 
 **request_staff_id** | **int**| A list of staff IDs that you want to retrieve payroll information for. If you do not supply a &#x60;StaffId&#x60;, all active staff members return, ordered by staff ID. | [optional] 
 **request_start_date_time** | **datetime**| The beginning of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.  * If you do not supply a &#x60;StartDateTime&#x60;, data returns for the seven days prior to the &#x60;EndDateTime&#x60; that you supply.  * If you do not supply either a &#x60;StartDateTime&#x60; or an &#x60;EndDateTime&#x60;, the data returns for seven days prior to today’s date. | [optional] 

### Return type

[**GetClassPayrollResponse**](GetClassPayrollResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payroll_get_time_clock**
> GetTimeClockResponse payroll_get_time_clock(site_id, version, authorization=authorization, request_end_date_time=request_end_date_time, request_include_inactive_staff=request_include_inactive_staff, request_limit=request_limit, request_offset=request_offset, request_staff_id=request_staff_id, request_start_date_time=request_start_date_time)

Get time card payroll for staff members.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PayrollApi()
site_id = 'site_id_example' # str | ID of the site from which to pull data.
version = 'version_example' # str | 
authorization = '' # str | A staff user authorization token. (optional) (default to )
request_end_date_time = '2013-10-20T19:20:30+01:00' # datetime | The end of the date range for the time card information to be returned. If you do not supply an `EndDateTime`, data returns for the seven days prior to today’s date. Classes that begin before the `EndDateTime` are included in the response, regardless of the time that the class ends. The maximum allowed date range is 14 days.<br />  Default: **Today’s date** (optional)
request_include_inactive_staff = true # bool | When `true`, payroll information returns for both active and inactive staff members.<br />  Default: **false** (optional)
request_limit = 56 # int | Number of results to include, defaults to 100 (optional)
request_offset = 56 # int | Page offset, defaults to 0. (optional)
request_staff_id = 789 # int | The staff ID for whom you want to retrieve time card information. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID. (optional)
request_start_date_time = '2013-10-20T19:20:30+01:00' # datetime | The beginning of the date range for the time card information to be returned. If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply. The maximum allowed date range is 14 days. (optional)

try:
    # Get time card payroll for staff members.
    api_response = api_instance.payroll_get_time_clock(site_id, version, authorization=authorization, request_end_date_time=request_end_date_time, request_include_inactive_staff=request_include_inactive_staff, request_limit=request_limit, request_offset=request_offset, request_staff_id=request_staff_id, request_start_date_time=request_start_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollApi->payroll_get_time_clock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| ID of the site from which to pull data. | 
 **version** | **str**|  | 
 **authorization** | **str**| A staff user authorization token. | [optional] [default to ]
 **request_end_date_time** | **datetime**| The end of the date range for the time card information to be returned. If you do not supply an &#x60;EndDateTime&#x60;, data returns for the seven days prior to today’s date. Classes that begin before the &#x60;EndDateTime&#x60; are included in the response, regardless of the time that the class ends. The maximum allowed date range is 14 days.&lt;br /&gt;  Default: **Today’s date** | [optional] 
 **request_include_inactive_staff** | **bool**| When &#x60;true&#x60;, payroll information returns for both active and inactive staff members.&lt;br /&gt;  Default: **false** | [optional] 
 **request_limit** | **int**| Number of results to include, defaults to 100 | [optional] 
 **request_offset** | **int**| Page offset, defaults to 0. | [optional] 
 **request_staff_id** | **int**| The staff ID for whom you want to retrieve time card information. If you do not supply a &#x60;StaffId&#x60;, all active staff members return, ordered by staff ID. | [optional] 
 **request_start_date_time** | **datetime**| The beginning of the date range for the time card information to be returned. If you do not supply a &#x60;StartDateTime&#x60;, data returns for the seven days prior to the &#x60;EndDateTime&#x60; that you supply. The maximum allowed date range is 14 days. | [optional] 

### Return type

[**GetTimeClockResponse**](GetTimeClockResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

