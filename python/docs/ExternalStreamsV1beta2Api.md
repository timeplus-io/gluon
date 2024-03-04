# swagger_client.ExternalStreamsV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_external_streams_get**](ExternalStreamsV1beta2Api.md#v1beta2_external_streams_get) | **GET** /v1beta2/external_streams | list external streams
[**v1beta2_external_streams_name_delete**](ExternalStreamsV1beta2Api.md#v1beta2_external_streams_name_delete) | **DELETE** /v1beta2/external_streams/{name} | delete an external stream
[**v1beta2_external_streams_name_get**](ExternalStreamsV1beta2Api.md#v1beta2_external_streams_name_get) | **GET** /v1beta2/external_streams/{name} | get an external stream
[**v1beta2_external_streams_post**](ExternalStreamsV1beta2Api.md#v1beta2_external_streams_post) | **POST** /v1beta2/external_streams | create an external stream

# **v1beta2_external_streams_get**
> list[ExternalStream] v1beta2_external_streams_get()

list external streams

Get all external streams.

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
api_instance = swagger_client.ExternalStreamsV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list external streams
    api_response = api_instance.v1beta2_external_streams_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalStreamsV1beta2Api->v1beta2_external_streams_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ExternalStream]**](ExternalStream.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_external_streams_name_delete**
> v1beta2_external_streams_name_delete(name)

delete an external stream

Delete the external stream with the given name.

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
api_instance = swagger_client.ExternalStreamsV1beta2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | external stream name

try:
    # delete an external stream
    api_instance.v1beta2_external_streams_name_delete(name)
except ApiException as e:
    print("Exception when calling ExternalStreamsV1beta2Api->v1beta2_external_streams_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| external stream name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_external_streams_name_get**
> ExternalStream v1beta2_external_streams_name_get(name)

get an external stream

Get the external stream with the given name.

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
api_instance = swagger_client.ExternalStreamsV1beta2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | external stream name

try:
    # get an external stream
    api_response = api_instance.v1beta2_external_streams_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalStreamsV1beta2Api->v1beta2_external_streams_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| external stream name | 

### Return type

[**ExternalStream**](ExternalStream.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_external_streams_post**
> ExternalStreamDef v1beta2_external_streams_post(body)

create an external stream

Create an external stream.

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
api_instance = swagger_client.ExternalStreamsV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.ExternalStreamDef() # ExternalStreamDef | create external stream request parameters

try:
    # create an external stream
    api_response = api_instance.v1beta2_external_streams_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalStreamsV1beta2Api->v1beta2_external_streams_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalStreamDef**](ExternalStreamDef.md)| create external stream request parameters | 

### Return type

[**ExternalStreamDef**](ExternalStreamDef.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

