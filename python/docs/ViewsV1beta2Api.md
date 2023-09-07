# swagger_client.ViewsV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_views_get**](ViewsV1beta2Api.md#v1beta2_views_get) | **GET** /v1beta2/views | list views
[**v1beta2_views_name_delete**](ViewsV1beta2Api.md#v1beta2_views_name_delete) | **DELETE** /v1beta2/views/{name} | delete a view
[**v1beta2_views_name_get**](ViewsV1beta2Api.md#v1beta2_views_name_get) | **GET** /v1beta2/views/{name} | get a view
[**v1beta2_views_name_patch**](ViewsV1beta2Api.md#v1beta2_views_name_patch) | **PATCH** /v1beta2/views/{name} | update a view
[**v1beta2_views_name_stats_get**](ViewsV1beta2Api.md#v1beta2_views_name_stats_get) | **GET** /v1beta2/views/{name}/stats | get the stats of a view
[**v1beta2_views_post**](ViewsV1beta2Api.md#v1beta2_views_post) | **POST** /v1beta2/views | create a view

# **v1beta2_views_get**
> list[View] v1beta2_views_get()

list views

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
api_instance = swagger_client.ViewsV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list views
    api_response = api_instance.v1beta2_views_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsV1beta2Api->v1beta2_views_get: %s\n" % e)
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

# **v1beta2_views_name_delete**
> v1beta2_views_name_delete(name)

delete a view

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
api_instance = swagger_client.ViewsV1beta2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | view name

try:
    # delete a view
    api_instance.v1beta2_views_name_delete(name)
except ApiException as e:
    print("Exception when calling ViewsV1beta2Api->v1beta2_views_name_delete: %s\n" % e)
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

# **v1beta2_views_name_get**
> View v1beta2_views_name_get(name)

get a view

Get a view with the given name.

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
api_instance = swagger_client.ViewsV1beta2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | view name

try:
    # get a view
    api_response = api_instance.v1beta2_views_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsV1beta2Api->v1beta2_views_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| view name | 

### Return type

[**View**](View.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_views_name_patch**
> v1beta2_views_name_patch(body, name)

update a view

Update the specific view with the given name. Updating the query of a materialized view is not allowed

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
api_instance = swagger_client.ViewsV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateViewRequest() # UpdateViewRequest | update view request parameters
name = 'name_example' # str | name of the view

try:
    # update a view
    api_instance.v1beta2_views_name_patch(body, name)
except ApiException as e:
    print("Exception when calling ViewsV1beta2Api->v1beta2_views_name_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateViewRequest**](UpdateViewRequest.md)| update view request parameters | 
 **name** | **str**| name of the view | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_views_name_stats_get**
> StreamStats v1beta2_views_name_stats_get(name)

get the stats of a view

Get the stats of a view with the given name.

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
api_instance = swagger_client.ViewsV1beta2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | view name

try:
    # get the stats of a view
    api_response = api_instance.v1beta2_views_name_stats_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsV1beta2Api->v1beta2_views_name_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| view name | 

### Return type

[**StreamStats**](StreamStats.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_views_post**
> View v1beta2_views_post(body)

create a view

Create a view. There are two different types of the view, please refer to the documentation of [view](https://docs.timeplus.com/view) for more details.

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
api_instance = swagger_client.ViewsV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateViewRequest() # CreateViewRequest | create view request parameters

try:
    # create a view
    api_response = api_instance.v1beta2_views_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsV1beta2Api->v1beta2_views_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateViewRequest**](CreateViewRequest.md)| create view request parameters | 

### Return type

[**View**](View.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

