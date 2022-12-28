# swagger_client.QueriesV1beta2Api

All URIs are relative to *//beta.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_queries_post**](QueriesV1beta2Api.md#v1beta2_queries_post) | **POST** /v1beta2/queries | execute a query.

# **v1beta2_queries_post**
> v1beta2_queries_post(body)

execute a query.

execute a query.

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
api_instance = swagger_client.QueriesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateQueryRequestV1Beta2() # CreateQueryRequestV1Beta2 | query request parameters

try:
    # execute a query.
    api_instance.v1beta2_queries_post(body)
except ApiException as e:
    print("Exception when calling QueriesV1beta2Api->v1beta2_queries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateQueryRequestV1Beta2**](CreateQueryRequestV1Beta2.md)| query request parameters | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

