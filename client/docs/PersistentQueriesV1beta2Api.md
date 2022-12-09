# timeplus_client.PersistentQueriesV1beta2Api

All URIs are relative to _https//beta.timeplus.cloud/{workspace-id}/api_

| Method                                                                                                              | HTTP request                                  | Description                                  |
| ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | -------------------------------------------- |
| [**v1beta2_persistent_queries_get**](PersistentQueriesV1beta2Api.md#v1beta2_persistent_queries_get)                 | **GET** /v1beta2/persistent-queries           | list persistent-queries.                     |
| [**v1beta2_persistent_queries_id_data_get**](PersistentQueriesV1beta2Api.md#v1beta2_persistent_queries_id_data_get) | **GET** /v1beta2/persistent-queries/{id}/data | stream persistent query result via websocket |
| [**v1beta2_persistent_queries_id_delete**](PersistentQueriesV1beta2Api.md#v1beta2_persistent_queries_id_delete)     | **DELETE** /v1beta2/persistent-queries/{id}   | delete a persistent query.                   |
| [**v1beta2_persistent_queries_id_get**](PersistentQueriesV1beta2Api.md#v1beta2_persistent_queries_id_get)           | **GET** /v1beta2/persistent-queries/{id}      | get a persistent query.                      |
| [**v1beta2_persistent_queries_post**](PersistentQueriesV1beta2Api.md#v1beta2_persistent_queries_post)               | **POST** /v1beta2/persistent-queries          | execute a persistent query.                  |

# **v1beta2_persistent_queries_get**

> list[QueryWithMetrics] v1beta2_persistent_queries_get()

list persistent-queries.

Get all persistent-queries.

### Example

```python
from __future__ import print_function
import time
import timeplus_client
from timeplus_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = timeplus_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = timeplus_client.PersistentQueriesV1beta2Api(timeplus_client.ApiClient(configuration))

try:
    # list persistent-queries.
    api_response = api_instance.v1beta2_persistent_queries_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersistentQueriesV1beta2Api->v1beta2_persistent_queries_get: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[QueryWithMetrics]**](QueryWithMetrics.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_persistent_queries_id_data_get**

> v1beta2_persistent_queries_id_data_get(id)

stream persistent query result via websocket

stream persistent query result via websocket

### Example

```python
from __future__ import print_function
import time
import timeplus_client
from timeplus_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timeplus_client.PersistentQueriesV1beta2Api()
id = 'id_example' # str | persistent query id

try:
    # stream persistent query result via websocket
    api_instance.v1beta2_persistent_queries_id_data_get(id)
except ApiException as e:
    print("Exception when calling PersistentQueriesV1beta2Api->v1beta2_persistent_queries_id_data_get: %s\n" % e)
```

### Parameters

| Name   | Type    | Description         | Notes |
| ------ | ------- | ------------------- | ----- |
| **id** | **str** | persistent query id |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_persistent_queries_id_delete**

> v1beta2_persistent_queries_id_delete(id)

delete a persistent query.

Delete the persistent query with the given ID.

### Example

```python
from __future__ import print_function
import time
import timeplus_client
from timeplus_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = timeplus_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = timeplus_client.PersistentQueriesV1beta2Api(timeplus_client.ApiClient(configuration))
id = 'id_example' # str | persistent query ID

try:
    # delete a persistent query.
    api_instance.v1beta2_persistent_queries_id_delete(id)
except ApiException as e:
    print("Exception when calling PersistentQueriesV1beta2Api->v1beta2_persistent_queries_id_delete: %s\n" % e)
```

### Parameters

| Name   | Type    | Description         | Notes |
| ------ | ------- | ------------------- | ----- |
| **id** | **str** | persistent query ID |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_persistent_queries_id_get**

> QueryWithMetrics v1beta2_persistent_queries_id_get(id)

get a persistent query.

Get the persistent query with the given ID.

### Example

```python
from __future__ import print_function
import time
import timeplus_client
from timeplus_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = timeplus_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = timeplus_client.PersistentQueriesV1beta2Api(timeplus_client.ApiClient(configuration))
id = 'id_example' # str | persistent query ID

try:
    # get a persistent query.
    api_response = api_instance.v1beta2_persistent_queries_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersistentQueriesV1beta2Api->v1beta2_persistent_queries_id_get: %s\n" % e)
```

### Parameters

| Name   | Type    | Description         | Notes |
| ------ | ------- | ------------------- | ----- |
| **id** | **str** | persistent query ID |

### Return type

[**QueryWithMetrics**](QueryWithMetrics.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_persistent_queries_post**

> Query v1beta2_persistent_queries_post(body)

execute a persistent query.

execute a persistent query.

### Example

```python
from __future__ import print_function
import time
import timeplus_client
from timeplus_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = timeplus_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = timeplus_client.PersistentQueriesV1beta2Api(timeplus_client.ApiClient(configuration))
body = timeplus_client.CreatePersistentQueryRequest() # CreatePersistentQueryRequest | persistent query request parameters

try:
    # execute a persistent query.
    api_response = api_instance.v1beta2_persistent_queries_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersistentQueriesV1beta2Api->v1beta2_persistent_queries_post: %s\n" % e)
```

### Parameters

| Name     | Type                                                                | Description                         | Notes |
| -------- | ------------------------------------------------------------------- | ----------------------------------- | ----- |
| **body** | [**CreatePersistentQueryRequest**](CreatePersistentQueryRequest.md) | persistent query request parameters |

### Return type

[**Query**](Query.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
