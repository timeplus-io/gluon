# swagger_client.ViewsV1beta1Api

All URIs are relative to *https//beta.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta1_views_get**](ViewsV1beta1Api.md#v1beta1_views_get) | **GET** /v1beta1/views | list views.
[**v1beta1_views_name_delete**](ViewsV1beta1Api.md#v1beta1_views_name_delete) | **DELETE** /v1beta1/views/{name} | delete a view.
[**v1beta1_views_post**](ViewsV1beta1Api.md#v1beta1_views_post) | **POST** /v1beta1/views | create a view.

# **v1beta1_views_get**
> list[View] v1beta1_views_get()

list views.

Get all views.

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
api_instance = swagger_client.ViewsV1beta1Api(swagger_client.ApiClient(configuration))

try:
    # list views.
    api_response = api_instance.v1beta1_views_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsV1beta1Api->v1beta1_views_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[View]**](View.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_views_name_delete**
> v1beta1_views_name_delete(name)

delete a view.

Delete the view with the given name.

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
api_instance = swagger_client.ViewsV1beta1Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | view name

try:
    # delete a view.
    api_instance.v1beta1_views_name_delete(name)
except ApiException as e:
    print("Exception when calling ViewsV1beta1Api->v1beta1_views_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| view name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_views_post**
> View v1beta1_views_post(body)

create a view.

Create a view.

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
api_instance = swagger_client.ViewsV1beta1Api(swagger_client.ApiClient(configuration))
body = swagger_client.View() # View | create view request parameters

try:
    # create a view.
    api_response = api_instance.v1beta1_views_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsV1beta1Api->v1beta1_views_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**View**](View.md)| create view request parameters | 

### Return type

[**View**](View.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

