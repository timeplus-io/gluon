# swagger_client.AlertsV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_alerts_id_stop_post**](AlertsV1beta2Api.md#v1beta2_alerts_id_stop_post) | **POST** /v1beta2/alerts/{id}/stop | stop an alert.

# **v1beta2_alerts_id_stop_post**
> v1beta2_alerts_id_stop_post(id)

stop an alert.

Stop the alert with the given ID.

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
api_instance = swagger_client.AlertsV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | alert ID

try:
    # stop an alert.
    api_instance.v1beta2_alerts_id_stop_post(id)
except ApiException as e:
    print("Exception when calling AlertsV1beta2Api->v1beta2_alerts_id_stop_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| alert ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

