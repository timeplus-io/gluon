# swagger_client.SinksV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_sinks_get**](SinksV1beta2Api.md#v1beta2_sinks_get) | **GET** /v1beta2/sinks | list sinks
[**v1beta2_sinks_id_delete**](SinksV1beta2Api.md#v1beta2_sinks_id_delete) | **DELETE** /v1beta2/sinks/{id} | delete a sink
[**v1beta2_sinks_id_get**](SinksV1beta2Api.md#v1beta2_sinks_id_get) | **GET** /v1beta2/sinks/{id} | get a sink
[**v1beta2_sinks_id_put**](SinksV1beta2Api.md#v1beta2_sinks_id_put) | **PUT** /v1beta2/sinks/{id} | update a sink
[**v1beta2_sinks_id_start_post**](SinksV1beta2Api.md#v1beta2_sinks_id_start_post) | **POST** /v1beta2/sinks/{id}/start | start a sink
[**v1beta2_sinks_id_stats_get**](SinksV1beta2Api.md#v1beta2_sinks_id_stats_get) | **GET** /v1beta2/sinks/{id}/stats | get the stats of a sink
[**v1beta2_sinks_id_stop_post**](SinksV1beta2Api.md#v1beta2_sinks_id_stop_post) | **POST** /v1beta2/sinks/{id}/stop | stop a sink
[**v1beta2_sinks_post**](SinksV1beta2Api.md#v1beta2_sinks_post) | **POST** /v1beta2/sinks | create a sink

# **v1beta2_sinks_get**
> list[Sink] v1beta2_sinks_get()

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
api_instance = swagger_client.SinksV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list sinks
    api_response = api_instance.v1beta2_sinks_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SinksV1beta2Api->v1beta2_sinks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Sink]**](Sink.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sinks_id_delete**
> v1beta2_sinks_id_delete(id)

delete a sink

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
api_instance = swagger_client.SinksV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | sink ID

try:
    # delete a sink
    api_instance.v1beta2_sinks_id_delete(id)
except ApiException as e:
    print("Exception when calling SinksV1beta2Api->v1beta2_sinks_id_delete: %s\n" % e)
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

# **v1beta2_sinks_id_get**
> Sink v1beta2_sinks_id_get(id)

get a sink

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
api_instance = swagger_client.SinksV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | sink ID

try:
    # get a sink
    api_response = api_instance.v1beta2_sinks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SinksV1beta2Api->v1beta2_sinks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| sink ID | 

### Return type

[**Sink**](Sink.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sinks_id_put**
> Sink v1beta2_sinks_id_put(body, id)

update a sink

Update the specific sink with the given ID.

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
api_instance = swagger_client.SinksV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSinkRequest() # CreateSinkRequest | update sink request parameters
id = 'id_example' # str | sink ID

try:
    # update a sink
    api_response = api_instance.v1beta2_sinks_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SinksV1beta2Api->v1beta2_sinks_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSinkRequest**](CreateSinkRequest.md)| update sink request parameters | 
 **id** | **str**| sink ID | 

### Return type

[**Sink**](Sink.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sinks_id_start_post**
> v1beta2_sinks_id_start_post(id)

start a sink

Start the sink with the given ID.

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
api_instance = swagger_client.SinksV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | sink ID

try:
    # start a sink
    api_instance.v1beta2_sinks_id_start_post(id)
except ApiException as e:
    print("Exception when calling SinksV1beta2Api->v1beta2_sinks_id_start_post: %s\n" % e)
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

# **v1beta2_sinks_id_stats_get**
> SinkStats v1beta2_sinks_id_stats_get(id, error_log_time_range, metrics_time_range)

get the stats of a sink

Get the stats of a sink with the given id.

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
api_instance = swagger_client.SinksV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | sink ID
error_log_time_range = 'error_log_time_range_example' # str | 
metrics_time_range = 'metrics_time_range_example' # str | 

try:
    # get the stats of a sink
    api_response = api_instance.v1beta2_sinks_id_stats_get(id, error_log_time_range, metrics_time_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SinksV1beta2Api->v1beta2_sinks_id_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| sink ID | 
 **error_log_time_range** | **str**|  | 
 **metrics_time_range** | **str**|  | 

### Return type

[**SinkStats**](SinkStats.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sinks_id_stop_post**
> v1beta2_sinks_id_stop_post(id)

stop a sink

Stop the sink with the given ID from sending out data.

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
api_instance = swagger_client.SinksV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | sink ID

try:
    # stop a sink
    api_instance.v1beta2_sinks_id_stop_post(id)
except ApiException as e:
    print("Exception when calling SinksV1beta2Api->v1beta2_sinks_id_stop_post: %s\n" % e)
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

# **v1beta2_sinks_post**
> Sink v1beta2_sinks_post(body)

create a sink

Create a sink. Please refer to the documentation of [sink](https://docs.timeplus.com/destination) for more details.

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
api_instance = swagger_client.SinksV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSinkRequest() # CreateSinkRequest | create sink request parameters

try:
    # create a sink
    api_response = api_instance.v1beta2_sinks_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SinksV1beta2Api->v1beta2_sinks_post: %s\n" % e)
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

