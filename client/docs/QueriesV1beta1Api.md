# timeplus_client.QueriesV1beta1Api

All URIs are relative to _https//beta.timeplus.cloud/{workspace-id}/api_

| Method                                                                                      | HTTP request                           | Description                                                                                |
| ------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------ |
| [**v1beta1_format_post**](QueriesV1beta1Api.md#v1beta1_format_post)                         | **POST** /v1beta1/format               | format a query.                                                                            |
| [**v1beta1_queries_get**](QueriesV1beta1Api.md#v1beta1_queries_get)                         | **GET** /v1beta1/queries               | list queries.                                                                              |
| [**v1beta1_queries_id_cancel_post**](QueriesV1beta1Api.md#v1beta1_queries_id_cancel_post)   | **POST** /v1beta1/queries/{id}/cancel  | cancel a query.                                                                            |
| [**v1beta1_queries_id_delete**](QueriesV1beta1Api.md#v1beta1_queries_id_delete)             | **DELETE** /v1beta1/queries/{id}       | delete a query.                                                                            |
| [**v1beta1_queries_id_get**](QueriesV1beta1Api.md#v1beta1_queries_id_get)                   | **GET** /v1beta1/queries/{id}          | get a query.                                                                               |
| [**v1beta1_queries_id_pipeline_get**](QueriesV1beta1Api.md#v1beta1_queries_id_pipeline_get) | **GET** /v1beta1/queries/{id}/pipeline | get the pipeline for a query                                                               |
| [**v1beta1_queries_post**](QueriesV1beta1Api.md#v1beta1_queries_post)                       | **POST** /v1beta1/queries              | execute a query.                                                                           |
| [**v1beta1_sqlanalyze_post**](QueriesV1beta1Api.md#v1beta1_sqlanalyze_post)                 | **POST** /v1beta1/sqlanalyze           | analyze sql                                                                                |
| [**ws_queries_id_get**](QueriesV1beta1Api.md#ws_queries_id_get)                             | **GET** /ws/queries/{id}               | stream query result via websocket [THIS API DOESN&#x27;T HAVE &#x60;v1beta1&#x60; IN PATH] |

# **v1beta1_format_post**

> FormatQueryResponse v1beta1_format_post(body)

format a query.

Format the given query and make it easy to read.

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
api_instance = timeplus_client.QueriesV1beta1Api(timeplus_client.ApiClient(configuration))
body = timeplus_client.FormatQueryRequest() # FormatQueryRequest | the query SQL to be formatted

try:
    # format a query.
    api_response = api_instance.v1beta1_format_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta1Api->v1beta1_format_post: %s\n" % e)
```

### Parameters

| Name     | Type                                            | Description                   | Notes |
| -------- | ----------------------------------------------- | ----------------------------- | ----- |
| **body** | [**FormatQueryRequest**](FormatQueryRequest.md) | the query SQL to be formatted |

### Return type

[**FormatQueryResponse**](FormatQueryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_queries_get**

> list[QueryWithMetrics] v1beta1_queries_get()

list queries.

Get all queries.

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
api_instance = timeplus_client.QueriesV1beta1Api(timeplus_client.ApiClient(configuration))

try:
    # list queries.
    api_response = api_instance.v1beta1_queries_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta1Api->v1beta1_queries_get: %s\n" % e)
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

# **v1beta1_queries_id_cancel_post**

> v1beta1_queries_id_cancel_post(id)

cancel a query.

Cancel the query with the given ID. If given query is not running, the request will do nothing. Otherwise, the query will be canceled and the `status` will be set to `canceled`

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
api_instance = timeplus_client.QueriesV1beta1Api(timeplus_client.ApiClient(configuration))
id = 'id_example' # str | query ID

try:
    # cancel a query.
    api_instance.v1beta1_queries_id_cancel_post(id)
except ApiException as e:
    print("Exception when calling QueriesV1beta1Api->v1beta1_queries_id_cancel_post: %s\n" % e)
```

### Parameters

| Name   | Type    | Description | Notes |
| ------ | ------- | ----------- | ----- |
| **id** | **str** | query ID    |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_queries_id_delete**

> v1beta1_queries_id_delete(id)

delete a query.

Delete the query with the given ID.

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
api_instance = timeplus_client.QueriesV1beta1Api(timeplus_client.ApiClient(configuration))
id = 'id_example' # str | query ID

try:
    # delete a query.
    api_instance.v1beta1_queries_id_delete(id)
except ApiException as e:
    print("Exception when calling QueriesV1beta1Api->v1beta1_queries_id_delete: %s\n" % e)
```

### Parameters

| Name   | Type    | Description | Notes |
| ------ | ------- | ----------- | ----- |
| **id** | **str** | query ID    |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_queries_id_get**

> QueryWithMetrics v1beta1_queries_id_get(id)

get a query.

Get the query with the given ID.

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
api_instance = timeplus_client.QueriesV1beta1Api(timeplus_client.ApiClient(configuration))
id = 'id_example' # str | query ID

try:
    # get a query.
    api_response = api_instance.v1beta1_queries_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta1Api->v1beta1_queries_id_get: %s\n" % e)
```

### Parameters

| Name   | Type    | Description | Notes |
| ------ | ------- | ----------- | ----- |
| **id** | **str** | query ID    |

### Return type

[**QueryWithMetrics**](QueryWithMetrics.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_queries_id_pipeline_get**

> QueryPipeline v1beta1_queries_id_pipeline_get(id)

get the pipeline for a query

get the pipeline for a query

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
api_instance = timeplus_client.QueriesV1beta1Api(timeplus_client.ApiClient(configuration))
id = 'id_example' # str | query ID

try:
    # get the pipeline for a query
    api_response = api_instance.v1beta1_queries_id_pipeline_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta1Api->v1beta1_queries_id_pipeline_get: %s\n" % e)
```

### Parameters

| Name   | Type    | Description | Notes |
| ------ | ------- | ----------- | ----- |
| **id** | **str** | query ID    |

### Return type

[**QueryPipeline**](QueryPipeline.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_queries_post**

> CreateQueryResponse v1beta1_queries_post(body)

execute a query.

execute a query.

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
api_instance = timeplus_client.QueriesV1beta1Api(timeplus_client.ApiClient(configuration))
body = timeplus_client.CreateQueryRequestV1Beta1() # CreateQueryRequestV1Beta1 | query request parameters

try:
    # execute a query.
    api_response = api_instance.v1beta1_queries_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta1Api->v1beta1_queries_post: %s\n" % e)
```

### Parameters

| Name     | Type                                                          | Description              | Notes |
| -------- | ------------------------------------------------------------- | ------------------------ | ----- |
| **body** | [**CreateQueryRequestV1Beta1**](CreateQueryRequestV1Beta1.md) | query request parameters |

### Return type

[**CreateQueryResponse**](CreateQueryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta1_sqlanalyze_post**

> SQLAnalyzeResult v1beta1_sqlanalyze_post(body)

analyze sql

analyze sql

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
api_instance = timeplus_client.QueriesV1beta1Api(timeplus_client.ApiClient(configuration))
body = timeplus_client.AnalyzeSQLRequest() # AnalyzeSQLRequest | sql request parameters

try:
    # analyze sql
    api_response = api_instance.v1beta1_sqlanalyze_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta1Api->v1beta1_sqlanalyze_post: %s\n" % e)
```

### Parameters

| Name     | Type                                          | Description            | Notes |
| -------- | --------------------------------------------- | ---------------------- | ----- |
| **body** | [**AnalyzeSQLRequest**](AnalyzeSQLRequest.md) | sql request parameters |

### Return type

[**SQLAnalyzeResult**](SQLAnalyzeResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ws_queries_id_get**

> ws_queries_id_get(id)

stream query result via websocket [THIS API DOESN'T HAVE `v1beta1` IN PATH]

stream query result via websocket

### Example

```python
from __future__ import print_function
import time
import timeplus_client
from timeplus_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timeplus_client.QueriesV1beta1Api()
id = 'id_example' # str | query id

try:
    # stream query result via websocket [THIS API DOESN'T HAVE `v1beta1` IN PATH]
    api_instance.ws_queries_id_get(id)
except ApiException as e:
    print("Exception when calling QueriesV1beta1Api->ws_queries_id_get: %s\n" % e)
```

### Parameters

| Name   | Type    | Description | Notes |
| ------ | ------- | ----------- | ----- |
| **id** | **str** | query id    |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
