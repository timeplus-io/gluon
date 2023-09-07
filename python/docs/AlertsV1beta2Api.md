# swagger_client.AlertsV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_alerts_get**](AlertsV1beta2Api.md#v1beta2_alerts_get) | **GET** /v1beta2/alerts | list alerts
[**v1beta2_alerts_id_delete**](AlertsV1beta2Api.md#v1beta2_alerts_id_delete) | **DELETE** /v1beta2/alerts/{id} | delete an alert
[**v1beta2_alerts_id_get**](AlertsV1beta2Api.md#v1beta2_alerts_id_get) | **GET** /v1beta2/alerts/{id} | get an alert
[**v1beta2_alerts_id_put**](AlertsV1beta2Api.md#v1beta2_alerts_id_put) | **PUT** /v1beta2/alerts/{id} | update an alert
[**v1beta2_alerts_id_resolve_post**](AlertsV1beta2Api.md#v1beta2_alerts_id_resolve_post) | **POST** /v1beta2/alerts/{id}/resolve | resolve a triggered alert
[**v1beta2_alerts_id_start_post**](AlertsV1beta2Api.md#v1beta2_alerts_id_start_post) | **POST** /v1beta2/alerts/{id}/start | start an alert
[**v1beta2_alerts_id_stop_post**](AlertsV1beta2Api.md#v1beta2_alerts_id_stop_post) | **POST** /v1beta2/alerts/{id}/stop | stop an alert
[**v1beta2_alerts_post**](AlertsV1beta2Api.md#v1beta2_alerts_post) | **POST** /v1beta2/alerts | create an alert

# **v1beta2_alerts_get**
> list[Alert] v1beta2_alerts_get()

list alerts

Get all alerts.

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
api_instance = swagger_client.AlertsV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list alerts
    api_response = api_instance.v1beta2_alerts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsV1beta2Api->v1beta2_alerts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Alert]**](Alert.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_alerts_id_delete**
> v1beta2_alerts_id_delete(id)

delete an alert

Delete the alert with the given ID.

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
api_instance = swagger_client.AlertsV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | alert ID

try:
    # delete an alert
    api_instance.v1beta2_alerts_id_delete(id)
except ApiException as e:
    print("Exception when calling AlertsV1beta2Api->v1beta2_alerts_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| alert ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_alerts_id_get**
> Alert v1beta2_alerts_id_get(id)

get an alert

Get an alert with the given ID.

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
api_instance = swagger_client.AlertsV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | alert ID

try:
    # get an alert
    api_response = api_instance.v1beta2_alerts_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsV1beta2Api->v1beta2_alerts_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| alert ID | 

### Return type

[**Alert**](Alert.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_alerts_id_put**
> Alert v1beta2_alerts_id_put(body, id)

update an alert

Update the specific alert with the given ID.

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
api_instance = swagger_client.AlertsV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateAlertRequest() # CreateAlertRequest | update alert request parameters
id = 'id_example' # str | alert ID

try:
    # update an alert
    api_response = api_instance.v1beta2_alerts_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsV1beta2Api->v1beta2_alerts_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAlertRequest**](CreateAlertRequest.md)| update alert request parameters | 
 **id** | **str**| alert ID | 

### Return type

[**Alert**](Alert.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_alerts_id_resolve_post**
> v1beta2_alerts_id_resolve_post(id)

resolve a triggered alert

Manually resolve a triggered alert so that it can be triggered again by the trigger event in the future.

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
api_instance = swagger_client.AlertsV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | alert ID

try:
    # resolve a triggered alert
    api_instance.v1beta2_alerts_id_resolve_post(id)
except ApiException as e:
    print("Exception when calling AlertsV1beta2Api->v1beta2_alerts_id_resolve_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| alert ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_alerts_id_start_post**
> v1beta2_alerts_id_start_post(id)

start an alert

Start the alert with the given ID. If the alert is already running, the API does nothing and returns 204.

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
api_instance = swagger_client.AlertsV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Alert ID

try:
    # start an alert
    api_instance.v1beta2_alerts_id_start_post(id)
except ApiException as e:
    print("Exception when calling AlertsV1beta2Api->v1beta2_alerts_id_start_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Alert ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_alerts_id_stop_post**
> v1beta2_alerts_id_stop_post(id)

stop an alert

Stop the alert with the given ID.

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
api_instance = swagger_client.AlertsV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | alert ID

try:
    # stop an alert
    api_instance.v1beta2_alerts_id_stop_post(id)
except ApiException as e:
    print("Exception when calling AlertsV1beta2Api->v1beta2_alerts_id_stop_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| alert ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_alerts_post**
> Alert v1beta2_alerts_post(body)

create an alert

Create an alert. Please refer to the documentation of [alert](https://docs.timeplus.com/alert) for more details.

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
api_instance = swagger_client.AlertsV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateAlertRequest() # CreateAlertRequest | create alert request parameters

try:
    # create an alert
    api_response = api_instance.v1beta2_alerts_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsV1beta2Api->v1beta2_alerts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAlertRequest**](CreateAlertRequest.md)| create alert request parameters | 

### Return type

[**Alert**](Alert.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

