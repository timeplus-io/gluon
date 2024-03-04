# swagger_client.SourcesV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_source_infer_post**](SourcesV1beta2Api.md#v1beta2_source_infer_post) | **POST** /v1beta2/source/infer | infer schema from an existing event
[**v1beta2_source_kafka_topics_post**](SourcesV1beta2Api.md#v1beta2_source_kafka_topics_post) | **POST** /v1beta2/source/kafka/topics | list Kafka topics
[**v1beta2_source_match_post**](SourcesV1beta2Api.md#v1beta2_source_match_post) | **POST** /v1beta2/source/match | return streams that are compatible with provided events
[**v1beta2_source_preview_post**](SourcesV1beta2Api.md#v1beta2_source_preview_post) | **POST** /v1beta2/source/preview | preview a source
[**v1beta2_sources_get**](SourcesV1beta2Api.md#v1beta2_sources_get) | **GET** /v1beta2/sources | list sources
[**v1beta2_sources_id_delete**](SourcesV1beta2Api.md#v1beta2_sources_id_delete) | **DELETE** /v1beta2/sources/{id} | delete a source
[**v1beta2_sources_id_get**](SourcesV1beta2Api.md#v1beta2_sources_id_get) | **GET** /v1beta2/sources/{id} | get a source
[**v1beta2_sources_id_put**](SourcesV1beta2Api.md#v1beta2_sources_id_put) | **PUT** /v1beta2/sources/{id} | update a source
[**v1beta2_sources_id_start_post**](SourcesV1beta2Api.md#v1beta2_sources_id_start_post) | **POST** /v1beta2/sources/{id}/start | start a source
[**v1beta2_sources_id_stats_get**](SourcesV1beta2Api.md#v1beta2_sources_id_stats_get) | **GET** /v1beta2/sources/{id}/stats | get the stats of a source
[**v1beta2_sources_id_stop_post**](SourcesV1beta2Api.md#v1beta2_sources_id_stop_post) | **POST** /v1beta2/sources/{id}/stop | stop a source
[**v1beta2_sources_post**](SourcesV1beta2Api.md#v1beta2_sources_post) | **POST** /v1beta2/sources | create a source

# **v1beta2_source_infer_post**
> EventInferResponse v1beta2_source_infer_post(body)

infer schema from an existing event

This endpoint returns the inferred schema for this particular event. The schema can be used to create a new stream to store events like this.

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
body = swagger_client.EventInferRequest() # EventInferRequest | event used to infer schema

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
 **body** | [**EventInferRequest**](EventInferRequest.md)| event used to infer schema | 

### Return type

[**EventInferResponse**](EventInferResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_source_kafka_topics_post**
> list[str] v1beta2_source_kafka_topics_post(body)

list Kafka topics

The request payload of this endpoint is the subset of the payload of create kafka source. Only certain `properties` is needed.

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
body = swagger_client.V1beta2ListKafkaTopicRequest() # V1beta2ListKafkaTopicRequest | kakfa server properties

try:
    # list Kafka topics
    api_response = api_instance.v1beta2_source_kafka_topics_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_source_kafka_topics_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta2ListKafkaTopicRequest**](V1beta2ListKafkaTopicRequest.md)| kakfa server properties | 

### Return type

**list[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_source_match_post**
> list[str] v1beta2_source_match_post(body)

return streams that are compatible with provided events

This endpoint can help you determine which stream(s) can be used to store those events.

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
    # return streams that are compatible with provided events
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

preview a source

Get sample events from the source with the given ID. Please refer to create source for more details regarding `type` and `properties`.

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
    # preview a source
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

# **v1beta2_sources_get**
> list[Source] v1beta2_sources_get()

list sources

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
    # list sources
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

delete a source

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
    # delete a source
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

get a source

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
    # get a source
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

update a source

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
    # update a source
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

start a source

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
    # start a source
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

# **v1beta2_sources_id_stats_get**
> Stats v1beta2_sources_id_stats_get(id, error_log_time_range, metrics_time_range)

get the stats of a source

Get the stats of a source with the given id.

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
error_log_time_range = 'error_log_time_range_example' # str | 
metrics_time_range = 'metrics_time_range_example' # str | 

try:
    # get the stats of a source
    api_response = api_instance.v1beta2_sources_id_stats_get(id, error_log_time_range, metrics_time_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesV1beta2Api->v1beta2_sources_id_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| source ID | 
 **error_log_time_range** | **str**|  | 
 **metrics_time_range** | **str**|  | 

### Return type

[**Stats**](Stats.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sources_id_stop_post**
> v1beta2_sources_id_stop_post(id)

stop a source

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
    # stop a source
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

create a source

Create a source. Please refer to the documentation of [source](https://docs.timeplus.com/source) for more details.

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
    # create a source
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

