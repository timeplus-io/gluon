# swagger_client.SavedQueriesV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_savedqueries_get**](SavedQueriesV1beta2Api.md#v1beta2_savedqueries_get) | **GET** /v1beta2/savedqueries | list Saved queries
[**v1beta2_savedqueries_id_delete**](SavedQueriesV1beta2Api.md#v1beta2_savedqueries_id_delete) | **DELETE** /v1beta2/savedqueries/{id} | delete a saved query
[**v1beta2_savedqueries_id_get**](SavedQueriesV1beta2Api.md#v1beta2_savedqueries_id_get) | **GET** /v1beta2/savedqueries/{id} | get a saved query
[**v1beta2_savedqueries_id_put**](SavedQueriesV1beta2Api.md#v1beta2_savedqueries_id_put) | **PUT** /v1beta2/savedqueries/{id} | update a saved query
[**v1beta2_savedqueries_post**](SavedQueriesV1beta2Api.md#v1beta2_savedqueries_post) | **POST** /v1beta2/savedqueries | create an saved query

# **v1beta2_savedqueries_get**
> list[SavedQuery] v1beta2_savedqueries_get()

list Saved queries

Get all saved queries

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
api_instance = swagger_client.SavedQueriesV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list Saved queries
    api_response = api_instance.v1beta2_savedqueries_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesV1beta2Api->v1beta2_savedqueries_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SavedQuery]**](SavedQuery.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_savedqueries_id_delete**
> v1beta2_savedqueries_id_delete(id)

delete a saved query

Delete the saved query with the givin ID

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
api_instance = swagger_client.SavedQueriesV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | saved query ID

try:
    # delete a saved query
    api_instance.v1beta2_savedqueries_id_delete(id)
except ApiException as e:
    print("Exception when calling SavedQueriesV1beta2Api->v1beta2_savedqueries_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| saved query ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_savedqueries_id_get**
> SavedQuery v1beta2_savedqueries_id_get(id)

get a saved query

Get a saved query.

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
api_instance = swagger_client.SavedQueriesV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | saved query ID

try:
    # get a saved query
    api_response = api_instance.v1beta2_savedqueries_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesV1beta2Api->v1beta2_savedqueries_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| saved query ID | 

### Return type

[**SavedQuery**](SavedQuery.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_savedqueries_id_put**
> SavedQuery v1beta2_savedqueries_id_put(body, id)

update a saved query

Update the specific saved query with the given ID.

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
api_instance = swagger_client.SavedQueriesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSavedQueryRequest() # CreateSavedQueryRequest | update saved query request parameters
id = 'id_example' # str | saved query ID

try:
    # update a saved query
    api_response = api_instance.v1beta2_savedqueries_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesV1beta2Api->v1beta2_savedqueries_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSavedQueryRequest**](CreateSavedQueryRequest.md)| update saved query request parameters | 
 **id** | **str**| saved query ID | 

### Return type

[**SavedQuery**](SavedQuery.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_savedqueries_post**
> SavedQuery v1beta2_savedqueries_post(body)

create an saved query

Create a new saved query.

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
api_instance = swagger_client.SavedQueriesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSavedQueryRequest() # CreateSavedQueryRequest | saved query parameters

try:
    # create an saved query
    api_response = api_instance.v1beta2_savedqueries_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesV1beta2Api->v1beta2_savedqueries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSavedQueryRequest**](CreateSavedQueryRequest.md)| saved query parameters | 

### Return type

[**SavedQuery**](SavedQuery.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

