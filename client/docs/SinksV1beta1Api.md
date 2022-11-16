# swagger_client.SinksV1beta1Api

All URIs are relative to *https//beta.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta1_sinks_get**](SinksV1beta1Api.md#v1beta1_sinks_get) | **GET** /v1beta1/sinks | list sinks
[**v1beta1_sinks_id_delete**](SinksV1beta1Api.md#v1beta1_sinks_id_delete) | **DELETE** /v1beta1/sinks/{id} | delete a sink.
[**v1beta1_sinks_id_get**](SinksV1beta1Api.md#v1beta1_sinks_id_get) | **GET** /v1beta1/sinks/{id} | get a sink.
[**v1beta1_sinks_post**](SinksV1beta1Api.md#v1beta1_sinks_post) | **POST** /v1beta1/sinks | create a sink.

# **v1beta1_sinks_get**
> list[SinkWithMetrics] v1beta1_sinks_get()

list sinks

Get all sinks

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
api_instance = swagger_client.SinksV1beta1Api(swagger_client.ApiClient(configuration))

try:
    # list sinks
    api_response = api_instance.v1beta1_sinks_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SinksV1beta1Api->v1beta1_sinks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SinkWithMetrics]**](SinkWithMetrics.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_sinks_id_delete**
> v1beta1_sinks_id_delete(id)

delete a sink.

Delete a sink with the given ID.

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
api_instance = swagger_client.SinksV1beta1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | sink ID

try:
    # delete a sink.
    api_instance.v1beta1_sinks_id_delete(id)
except ApiException as e:
    print("Exception when calling SinksV1beta1Api->v1beta1_sinks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| sink ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_sinks_id_get**
> SinkWithMetrics v1beta1_sinks_id_get(id)

get a sink.

Get a sink with the given ID.

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
api_instance = swagger_client.SinksV1beta1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | sink ID

try:
    # get a sink.
    api_response = api_instance.v1beta1_sinks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SinksV1beta1Api->v1beta1_sinks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| sink ID | 

### Return type

[**SinkWithMetrics**](SinkWithMetrics.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_sinks_post**
> Sink v1beta1_sinks_post(body)

create a sink.

Create a sink.

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
api_instance = swagger_client.SinksV1beta1Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSinkRequest() # CreateSinkRequest | create sink request parameters

try:
    # create a sink.
    api_response = api_instance.v1beta1_sinks_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SinksV1beta1Api->v1beta1_sinks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSinkRequest**](CreateSinkRequest.md)| create sink request parameters | 

### Return type

[**Sink**](Sink.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
