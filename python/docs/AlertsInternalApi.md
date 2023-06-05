# swagger_client.AlertsInternalApi

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_internal_tenants_tenant_alerts_id_start_post**](AlertsInternalApi.md#api_internal_tenants_tenant_alerts_id_start_post) | **POST** /api/internal/tenants/{tenant}/alerts/{id}/start | start an alert.

# **api_internal_tenants_tenant_alerts_id_start_post**
> api_internal_tenants_tenant_alerts_id_start_post(id)

start an alert.

Start the alert with the given ID. If the alert is already running, the API does nothing and returns 204.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AlertsInternalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Alert ID

try:
    # start an alert.
    api_instance.api_internal_tenants_tenant_alerts_id_start_post(id)
except ApiException as e:
    print("Exception when calling AlertsInternalApi->api_internal_tenants_tenant_alerts_id_start_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Alert ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

