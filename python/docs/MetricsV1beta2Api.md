# swagger_client.MetricsV1beta2Api

All URIs are relative to *//beta.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_global_metrics_post**](MetricsV1beta2Api.md#v1beta2_global_metrics_post) | **POST** /v1beta2/global_metrics | query global metrics.
[**v1beta2_resource_metrics_post**](MetricsV1beta2Api.md#v1beta2_resource_metrics_post) | **POST** /v1beta2/resource_metrics | query resource metrics.

# **v1beta2_global_metrics_post**
> GlobalMetricsResult v1beta2_global_metrics_post(body)

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
body = swagger_client.InternalHttpHandlerV1beta2GlobalMetricsRequest() # InternalHttpHandlerV1beta2GlobalMetricsRequest | metrics query request parameters

try:
    # query global metrics.
    api_response = api_instance.v1beta2_global_metrics_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsV1beta2Api->v1beta2_global_metrics_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InternalHttpHandlerV1beta2GlobalMetricsRequest**](InternalHttpHandlerV1beta2GlobalMetricsRequest.md)| metrics query request parameters | 

### Return type

[**GlobalMetricsResult**](GlobalMetricsResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_resource_metrics_post**
> ResourceMetricsResult v1beta2_resource_metrics_post(body)

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
body = swagger_client.InternalHttpHandlerV1beta2GlobalMetricsRequest() # InternalHttpHandlerV1beta2GlobalMetricsRequest | metrics query request parameters

try:
    # query resource metrics.
    api_response = api_instance.v1beta2_resource_metrics_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsV1beta2Api->v1beta2_resource_metrics_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InternalHttpHandlerV1beta2GlobalMetricsRequest**](InternalHttpHandlerV1beta2GlobalMetricsRequest.md)| metrics query request parameters | 

### Return type

[**ResourceMetricsResult**](ResourceMetricsResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

