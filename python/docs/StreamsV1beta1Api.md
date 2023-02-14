# swagger_client.StreamsV1beta1Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta1_streams_external_post**](StreamsV1beta1Api.md#v1beta1_streams_external_post) | **POST** /v1beta1/streams/external | create an external stream.
[**v1beta1_streams_get**](StreamsV1beta1Api.md#v1beta1_streams_get) | **GET** /v1beta1/streams | list streams.
[**v1beta1_streams_name_delete**](StreamsV1beta1Api.md#v1beta1_streams_name_delete) | **DELETE** /v1beta1/streams/{name} | delete a stream.
[**v1beta1_streams_name_ingest_post**](StreamsV1beta1Api.md#v1beta1_streams_name_ingest_post) | **POST** /v1beta1/streams/{name}/ingest | ingest data.
[**v1beta1_streams_name_patch**](StreamsV1beta1Api.md#v1beta1_streams_name_patch) | **PATCH** /v1beta1/streams/{name} | Update a stream.
[**v1beta1_streams_post**](StreamsV1beta1Api.md#v1beta1_streams_post) | **POST** /v1beta1/streams | create a stream.

# **v1beta1_streams_external_post**
> ExternalStreamDef v1beta1_streams_external_post(body)

create an external stream.

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
api_instance = swagger_client.StreamsV1beta1Api(swagger_client.ApiClient(configuration))
body = swagger_client.ExternalStreamDef() # ExternalStreamDef | create external stream request parameters

try:
    # create an external stream.
    api_response = api_instance.v1beta1_streams_external_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamsV1beta1Api->v1beta1_streams_external_post: %s\n" % e)
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

# **v1beta1_streams_get**
> list[Stream] v1beta1_streams_get()

list streams.

Get all streams.

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
api_instance = swagger_client.StreamsV1beta1Api(swagger_client.ApiClient(configuration))

try:
    # list streams.
    api_response = api_instance.v1beta1_streams_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamsV1beta1Api->v1beta1_streams_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Stream]**](Stream.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_streams_name_delete**
> v1beta1_streams_name_delete(name)

delete a stream.

Delete the stream with the given name.

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
api_instance = swagger_client.StreamsV1beta1Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | stream name

try:
    # delete a stream.
    api_instance.v1beta1_streams_name_delete(name)
except ApiException as e:
    print("Exception when calling StreamsV1beta1Api->v1beta1_streams_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| stream name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_streams_name_ingest_post**
> v1beta1_streams_name_ingest_post(body, name, format=format)

ingest data.

Ingest data to a stream with the given name. For formats are supported: * compact JSON: when `Content-Type` is set to one of `application/json`, `application/json;format=compact`, `application/vnd.timeplus+json`, `application/vnd.timeplus+json;format=compat`, or set `format` query parameter with value `compact`. And this is the API's default format. * JSON stream: when `Content-Type` is set to one of `application/json;format=streaming`, `application/vnd.timeplus+json;format=streaming`, or set `format` query parameter with value `streaming`. * raw string: when `Content-Type` is set to one of `text/plain`, `text/plain;format=raw`, or set `format` query parameter with value `raw`. * string lines: when `Content-Type` is set to `text/plain;format=lines`, or set `format` query parameter with value `lines`. 

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
api_instance = swagger_client.StreamsV1beta1Api(swagger_client.ApiClient(configuration))
body = swagger_client.IngestData() # IngestData | ingest data
name = 'name_example' # str | stream name
format = 'format_example' # str | enfoce payload format, if it is set, it overwrite the Content-Type header (optional)

try:
    # ingest data.
    api_instance.v1beta1_streams_name_ingest_post(body, name, format=format)
except ApiException as e:
    print("Exception when calling StreamsV1beta1Api->v1beta1_streams_name_ingest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IngestData**](IngestData.md)| ingest data | 
 **name** | **str**| stream name | 
 **format** | **str**| enfoce payload format, if it is set, it overwrite the Content-Type header | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.timeplus+json, application/json;format=compat, application/vnd.timeplus+json;format=compat, application/json;format=stream, application/vnd.timeplus+json;format=stream, application/x-ndjson, text/plain, text/plain;format=raw, text/plain;format=lines
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_streams_name_patch**
> v1beta1_streams_name_patch(body, name)

Update a stream.

Update the specific stream with the given name.

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
api_instance = swagger_client.StreamsV1beta1Api(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateStreamRequest() # UpdateStreamRequest | update stream request parameters
name = 'name_example' # str | name of the stream

try:
    # Update a stream.
    api_instance.v1beta1_streams_name_patch(body, name)
except ApiException as e:
    print("Exception when calling StreamsV1beta1Api->v1beta1_streams_name_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateStreamRequest**](UpdateStreamRequest.md)| update stream request parameters | 
 **name** | **str**| name of the stream | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_streams_post**
> StreamDef v1beta1_streams_post(body)

create a stream.

Create a stream.

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
api_instance = swagger_client.StreamsV1beta1Api(swagger_client.ApiClient(configuration))
body = swagger_client.StreamDef() # StreamDef | create stream request parameters

try:
    # create a stream.
    api_response = api_instance.v1beta1_streams_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamsV1beta1Api->v1beta1_streams_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StreamDef**](StreamDef.md)| create stream request parameters | 

### Return type

[**StreamDef**](StreamDef.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

