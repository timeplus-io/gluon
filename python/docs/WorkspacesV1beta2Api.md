# swagger_client.WorkspacesV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destroy_post**](WorkspacesV1beta2Api.md#destroy_post) | **POST** /destroy | delete the current workspace

# **destroy_post**
> destroy_post()

delete the current workspace

Completely delete the workspace. DANGEROUS: all data will be destroyed.

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
api_instance = swagger_client.WorkspacesV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # delete the current workspace
    api_instance.destroy_post()
except ApiException as e:
    print("Exception when calling WorkspacesV1beta2Api->destroy_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

