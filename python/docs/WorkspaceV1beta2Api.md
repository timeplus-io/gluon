# swagger_client.WorkspaceV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_workspace_get**](WorkspaceV1beta2Api.md#v1beta2_workspace_get) | **GET** /v1beta2/workspace | get current workspace
[**v1beta2_workspace_patch**](WorkspaceV1beta2Api.md#v1beta2_workspace_patch) | **PATCH** /v1beta2/workspace | update current workspace

# **v1beta2_workspace_get**
> Workspace v1beta2_workspace_get()

get current workspace

Get the basic information about the current workspace.

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
api_instance = swagger_client.WorkspaceV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # get current workspace
    api_response = api_instance.v1beta2_workspace_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspaceV1beta2Api->v1beta2_workspace_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Workspace**](Workspace.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_workspace_patch**
> v1beta2_workspace_patch(body)

update current workspace

Update the settings of current workspace

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
api_instance = swagger_client.WorkspaceV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateWorkspaceRequest() # UpdateWorkspaceRequest | update workspace request parameters

try:
    # update current workspace
    api_instance.v1beta2_workspace_patch(body)
except ApiException as e:
    print("Exception when calling WorkspaceV1beta2Api->v1beta2_workspace_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWorkspaceRequest**](UpdateWorkspaceRequest.md)| update workspace request parameters | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

