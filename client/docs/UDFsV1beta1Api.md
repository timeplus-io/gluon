# swagger_client.UDFsV1beta1Api

All URIs are relative to *https//beta.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta1_udfs_get**](UDFsV1beta1Api.md#v1beta1_udfs_get) | **GET** /v1beta1/udfs | list udf.
[**v1beta1_udfs_name_delete**](UDFsV1beta1Api.md#v1beta1_udfs_name_delete) | **DELETE** /v1beta1/udfs/{name} | delete a udf.
[**v1beta1_udfs_name_get**](UDFsV1beta1Api.md#v1beta1_udfs_name_get) | **GET** /v1beta1/udfs/{name} | get a udf.
[**v1beta1_udfs_post**](UDFsV1beta1Api.md#v1beta1_udfs_post) | **POST** /v1beta1/udfs | create a udf.

# **v1beta1_udfs_get**
> list[UDF] v1beta1_udfs_get()

list udf.

Get all udf.

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
api_instance = swagger_client.UDFsV1beta1Api(swagger_client.ApiClient(configuration))

try:
    # list udf.
    api_response = api_instance.v1beta1_udfs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UDFsV1beta1Api->v1beta1_udfs_get: %s\n" % e)
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

# **v1beta1_udfs_name_delete**
> v1beta1_udfs_name_delete(name)

delete a udf.

Delete the udf with the given name.

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
api_instance = swagger_client.UDFsV1beta1Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | udf name

try:
    # delete a udf.
    api_instance.v1beta1_udfs_name_delete(name)
except ApiException as e:
    print("Exception when calling UDFsV1beta1Api->v1beta1_udfs_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| udf name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_udfs_name_get**
> UDF v1beta1_udfs_name_get(name)

get a udf.

get the udf with the given name.

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
api_instance = swagger_client.UDFsV1beta1Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | udf name

try:
    # get a udf.
    api_response = api_instance.v1beta1_udfs_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UDFsV1beta1Api->v1beta1_udfs_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| udf name | 

### Return type

[**UDF**](UDF.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_udfs_post**
> UDF v1beta1_udfs_post(body)

create a udf.

Create a udf.

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
api_instance = swagger_client.UDFsV1beta1Api(swagger_client.ApiClient(configuration))
body = swagger_client.UDF() # UDF | create udf request parameters

try:
    # create a udf.
    api_response = api_instance.v1beta1_udfs_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UDFsV1beta1Api->v1beta1_udfs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UDF**](UDF.md)| create udf request parameters | 

### Return type

[**UDF**](UDF.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

