# swagger_client.UDFsV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_udfs_get**](UDFsV1beta2Api.md#v1beta2_udfs_get) | **GET** /v1beta2/udfs | list user-defined functions
[**v1beta2_udfs_name_delete**](UDFsV1beta2Api.md#v1beta2_udfs_name_delete) | **DELETE** /v1beta2/udfs/{name} | delete an user-defined function
[**v1beta2_udfs_name_get**](UDFsV1beta2Api.md#v1beta2_udfs_name_get) | **GET** /v1beta2/udfs/{name} | get an user-defined function
[**v1beta2_udfs_name_put**](UDFsV1beta2Api.md#v1beta2_udfs_name_put) | **PUT** /v1beta2/udfs/{name} | update an user-defined function
[**v1beta2_udfs_post**](UDFsV1beta2Api.md#v1beta2_udfs_post) | **POST** /v1beta2/udfs | create an user-defined function

# **v1beta2_udfs_get**
> list[UDF] v1beta2_udfs_get()

list user-defined functions

Get all user-defined functions.

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
api_instance = swagger_client.UDFsV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list user-defined functions
    api_response = api_instance.v1beta2_udfs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UDFsV1beta2Api->v1beta2_udfs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UDF]**](UDF.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_udfs_name_delete**
> v1beta2_udfs_name_delete(name)

delete an user-defined function

Delete the user-defined function with the given name.

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
api_instance = swagger_client.UDFsV1beta2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | user-defined function name

try:
    # delete an user-defined function
    api_instance.v1beta2_udfs_name_delete(name)
except ApiException as e:
    print("Exception when calling UDFsV1beta2Api->v1beta2_udfs_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| user-defined function name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_udfs_name_get**
> UDF v1beta2_udfs_name_get(name)

get an user-defined function

get the user-defined function with the given name.

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
api_instance = swagger_client.UDFsV1beta2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | user-defined function name

try:
    # get an user-defined function
    api_response = api_instance.v1beta2_udfs_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UDFsV1beta2Api->v1beta2_udfs_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| user-defined function name | 

### Return type

[**UDF**](UDF.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_udfs_name_put**
> UDF v1beta2_udfs_name_put(body)

update an user-defined function

Update the specific user-defined function with the given name.

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
api_instance = swagger_client.UDFsV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.UDF() # UDF | update UDF request parameters

try:
    # update an user-defined function
    api_response = api_instance.v1beta2_udfs_name_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UDFsV1beta2Api->v1beta2_udfs_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UDF**](UDF.md)| update UDF request parameters | 

### Return type

[**UDF**](UDF.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_udfs_post**
> UDF v1beta2_udfs_post(body)

create an user-defined function

Create an user-defined function.

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
api_instance = swagger_client.UDFsV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.UDF() # UDF | create UDF request parameters

try:
    # create an user-defined function
    api_response = api_instance.v1beta2_udfs_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UDFsV1beta2Api->v1beta2_udfs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UDF**](UDF.md)| create UDF request parameters | 

### Return type

[**UDF**](UDF.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

