# swagger_client.SourcesV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_source_infer_post**](SourcesV1beta2Api.md#v1beta2_source_infer_post) | **POST** /v1beta2/source/infer | infer schema from an existing event
[**v1beta2_source_match_post**](SourcesV1beta2Api.md#v1beta2_source_match_post) | **POST** /v1beta2/source/match | return streams match provided events
[**v1beta2_source_preview_post**](SourcesV1beta2Api.md#v1beta2_source_preview_post) | **POST** /v1beta2/source/preview | preview a source.
[**v1beta2_source_upload_post**](SourcesV1beta2Api.md#v1beta2_source_upload_post) | **POST** /v1beta2/source/upload | upload a file
[**v1beta2_sources_get**](SourcesV1beta2Api.md#v1beta2_sources_get) | **GET** /v1beta2/sources | list sources.
[**v1beta2_sources_id_delete**](SourcesV1beta2Api.md#v1beta2_sources_id_delete) | **DELETE** /v1beta2/sources/{id} | delete a source.
[**v1beta2_sources_id_get**](SourcesV1beta2Api.md#v1beta2_sources_id_get) | **GET** /v1beta2/sources/{id} | get a source.
[**v1beta2_sources_id_put**](SourcesV1beta2Api.md#v1beta2_sources_id_put) | **PUT** /v1beta2/sources/{id} | Update a source.
[**v1beta2_sources_id_start_post**](SourcesV1beta2Api.md#v1beta2_sources_id_start_post) | **POST** /v1beta2/sources/{id}/start | start a source.
[**v1beta2_sources_id_stop_post**](SourcesV1beta2Api.md#v1beta2_sources_id_stop_post) | **POST** /v1beta2/sources/{id}/stop | stop a source.
[**v1beta2_sources_post**](SourcesV1beta2Api.md#v1beta2_sources_post) | **POST** /v1beta2/sources | create a source.

# **v1beta2_source_infer_post**
> list[EventInferResponse] v1beta2_source_infer_post(body)

infer schema from an existing event

infer schema from an existing event

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
api_instance = swagger_client.SourcesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.EventInferRequest() # EventInferRequest | events used to infer schema

try:
    # infer schema from an existing event
    api_response = api_instance.v1beta2_source_infer_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_source_infer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventInferRequest**](EventInferRequest.md)| events used to infer schema | 

### Return type

[**list[EventInferResponse]**](EventInferResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_source_match_post**
> list[str] v1beta2_source_match_post(body)

return streams match provided events

return streams match provided events

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
api_instance = swagger_client.SourcesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.StreamMatchRequest() # StreamMatchRequest | events to match

try:
    # return streams match provided events
    api_response = api_instance.v1beta2_source_match_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_source_match_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StreamMatchRequest**](StreamMatchRequest.md)| events to match | 

### Return type

**list[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_source_preview_post**
> list[Event] v1beta2_source_preview_post(body)

preview a source.

Get sample events from the source with the given ID.

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
api_instance = swagger_client.SourcesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.SourcePreviewRequest() # SourcePreviewRequest | source propeties for preview

try:
    # preview a source.
    api_response = api_instance.v1beta2_source_preview_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_source_preview_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourcePreviewRequest**](SourcePreviewRequest.md)| source propeties for preview | 

### Return type

[**list[Event]**](Event.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_source_upload_post**
> FileUploadResponse v1beta2_source_upload_post(body)

upload a file

Upload a file to the system.

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
api_instance = swagger_client.SourcesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.SourceUploadBody() # SourceUploadBody | 

try:
    # upload a file
    api_response = api_instance.v1beta2_source_upload_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_source_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceUploadBody**](SourceUploadBody.md)|  | 

### Return type

[**FileUploadResponse**](FileUploadResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sources_get**
> list[Source] v1beta2_sources_get()

list sources.

Get all sources.

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
api_instance = swagger_client.SourcesV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list sources.
    api_response = api_instance.v1beta2_sources_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_sources_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Source]**](Source.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sources_id_delete**
> v1beta2_sources_id_delete(id)

delete a source.

Delete the source with the given ID.

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
api_instance = swagger_client.SourcesV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | source ID

try:
    # delete a source.
    api_instance.v1beta2_sources_id_delete(id)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_sources_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| source ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sources_id_get**
> Source v1beta2_sources_id_get(id)

get a source.

Get a source with the given ID.

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
api_instance = swagger_client.SourcesV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | source ID

try:
    # get a source.
    api_response = api_instance.v1beta2_sources_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_sources_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| source ID | 

### Return type

[**Source**](Source.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sources_id_put**
> Source v1beta2_sources_id_put(body, id)

Update a source.

Update the specific source with the given ID. Only stopped sources can be updated.

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
api_instance = swagger_client.SourcesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateSourceRequest() # UpdateSourceRequest | update source request parameters
id = 'id_example' # str | source ID

try:
    # Update a source.
    api_response = api_instance.v1beta2_sources_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_sources_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSourceRequest**](UpdateSourceRequest.md)| update source request parameters | 
 **id** | **str**| source ID | 

### Return type

[**Source**](Source.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sources_id_start_post**
> v1beta2_sources_id_start_post(id)

start a source.

Start the source with the given ID.

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
api_instance = swagger_client.SourcesV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | source ID

try:
    # start a source.
    api_instance.v1beta2_sources_id_start_post(id)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_sources_id_start_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| source ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sources_id_stop_post**
> v1beta2_sources_id_stop_post(id)

stop a source.

Stop the source with the given ID.

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
api_instance = swagger_client.SourcesV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | source ID

try:
    # stop a source.
    api_instance.v1beta2_sources_id_stop_post(id)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_sources_id_stop_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| source ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sources_post**
> Source v1beta2_sources_post(body)

create a source.

Create a source.

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
api_instance = swagger_client.SourcesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSourceRequest() # CreateSourceRequest | create source request parameters

try:
    # create a source.
    api_response = api_instance.v1beta2_sources_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_sources_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSourceRequest**](CreateSourceRequest.md)| create source request parameters | 

### Return type

[**Source**](Source.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

