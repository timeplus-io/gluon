# swagger_client.MetricsV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_global_metrics_get**](MetricsV1beta2Api.md#v1beta2_global_metrics_get) | **GET** /v1beta2/global-metrics | query global metrics.
[**v1beta2_resource_metrics_get**](MetricsV1beta2Api.md#v1beta2_resource_metrics_get) | **GET** /v1beta2/resource-metrics | query resource metrics.

# **v1beta2_global_metrics_get**
> GlobalMetricsResult v1beta2_global_metrics_get()

query global metrics.

query global metrics..

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
api_instance = swagger_client.MetricsV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # query global metrics.
    api_response = api_instance.v1beta2_global_metrics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsV1beta2Api->v1beta2_global_metrics_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GlobalMetricsResult**](GlobalMetricsResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_resource_metrics_get**
> ResourceMetricsResult v1beta2_resource_metrics_get(metrics_type, resource_ids, time_range)

query resource metrics.

query resource metrics..

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
api_instance = swagger_client.MetricsV1beta2Api(swagger_client.ApiClient(configuration))
metrics_type = 'metrics_type_example' # str | 
resource_ids = ['resource_ids_example'] # list[str] | 
time_range = 56 # int | 

try:
    # query resource metrics.
    api_response = api_instance.v1beta2_resource_metrics_get(metrics_type, resource_ids, time_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsV1beta2Api->v1beta2_resource_metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics_type** | **str**|  | 
 **resource_ids** | [**list[str]**](str.md)|  | 
 **time_range** | **int**|  | 

### Return type

[**ResourceMetricsResult**](ResourceMetricsResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

