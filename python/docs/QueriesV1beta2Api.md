# swagger_client.QueriesV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_format_post**](QueriesV1beta2Api.md#v1beta2_format_post) | **POST** /v1beta2/format | format a query
[**v1beta2_queries_exec_post**](QueriesV1beta2Api.md#v1beta2_queries_exec_post) | **POST** /v1beta2/queries/exec | execute a DDL query
[**v1beta2_queries_get**](QueriesV1beta2Api.md#v1beta2_queries_get) | **GET** /v1beta2/queries | list queries
[**v1beta2_queries_id_cancel_post**](QueriesV1beta2Api.md#v1beta2_queries_id_cancel_post) | **POST** /v1beta2/queries/{id}/cancel | cancel a query
[**v1beta2_queries_id_delete**](QueriesV1beta2Api.md#v1beta2_queries_id_delete) | **DELETE** /v1beta2/queries/{id} | delete a query
[**v1beta2_queries_id_get**](QueriesV1beta2Api.md#v1beta2_queries_id_get) | **GET** /v1beta2/queries/{id} | get a query
[**v1beta2_queries_id_pipeline_get**](QueriesV1beta2Api.md#v1beta2_queries_id_pipeline_get) | **GET** /v1beta2/queries/{id}/pipeline | get the pipeline for a query
[**v1beta2_queries_post**](QueriesV1beta2Api.md#v1beta2_queries_post) | **POST** /v1beta2/queries | execute a query and return the results
[**v1beta2_sqlanalyze_post**](QueriesV1beta2Api.md#v1beta2_sqlanalyze_post) | **POST** /v1beta2/sqlanalyze | analyze sql

# **v1beta2_format_post**
> FormatQueryResponse v1beta2_format_post(body)

format a query

Format the given query and make it easy to read.

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
api_instance = swagger_client.QueriesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.FormatQueryRequest() # FormatQueryRequest | the query SQL to be formatted

try:
    # format a query
    api_response = api_instance.v1beta2_format_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta2Api->v1beta2_format_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormatQueryRequest**](FormatQueryRequest.md)| the query SQL to be formatted | 

### Return type

[**FormatQueryResponse**](FormatQueryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_queries_exec_post**
> Query v1beta2_queries_exec_post(body)

execute a DDL query

Execute a DDL query. Currently only create external stream is supported.

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
api_instance = swagger_client.QueriesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.ExecuteQueryRequest() # ExecuteQueryRequest | query request parameters

try:
    # execute a DDL query
    api_response = api_instance.v1beta2_queries_exec_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta2Api->v1beta2_queries_exec_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExecuteQueryRequest**](ExecuteQueryRequest.md)| query request parameters | 

### Return type

[**Query**](Query.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_queries_get**
> list[Query] v1beta2_queries_get(tag=tag)

list queries

Get all queries.

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
api_instance = swagger_client.QueriesV1beta2Api(swagger_client.ApiClient(configuration))
tag = 'tag_example' # str | filter by tag (optional)

try:
    # list queries
    api_response = api_instance.v1beta2_queries_get(tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta2Api->v1beta2_queries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| filter by tag | [optional] 

### Return type

[**list[Query]**](Query.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_queries_id_cancel_post**
> v1beta2_queries_id_cancel_post(id)

cancel a query

Cancel the query with the given ID. If given query is not running, the request will do nothing. Otherwise, the query will be canceled and the `status` will be set to `canceled`

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
api_instance = swagger_client.QueriesV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | query ID

try:
    # cancel a query
    api_instance.v1beta2_queries_id_cancel_post(id)
except ApiException as e:
    print("Exception when calling QueriesV1beta2Api->v1beta2_queries_id_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| query ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_queries_id_delete**
> v1beta2_queries_id_delete(id)

delete a query

Delete the query with the given ID.

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
api_instance = swagger_client.QueriesV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | query ID

try:
    # delete a query
    api_instance.v1beta2_queries_id_delete(id)
except ApiException as e:
    print("Exception when calling QueriesV1beta2Api->v1beta2_queries_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| query ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_queries_id_get**
> Query v1beta2_queries_id_get(id)

get a query

Get the query with the given ID.

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
api_instance = swagger_client.QueriesV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | query ID

try:
    # get a query
    api_response = api_instance.v1beta2_queries_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta2Api->v1beta2_queries_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| query ID | 

### Return type

[**Query**](Query.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_queries_id_pipeline_get**
> QueryPipeline v1beta2_queries_id_pipeline_get(id)

get the pipeline for a query

get the pipeline for a query

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
api_instance = swagger_client.QueriesV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | query ID

try:
    # get the pipeline for a query
    api_response = api_instance.v1beta2_queries_id_pipeline_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta2Api->v1beta2_queries_id_pipeline_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| query ID | 

### Return type

[**QueryPipeline**](QueryPipeline.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_queries_post**
> Query v1beta2_queries_post(body)

execute a query and return the results

Execute a query and return the results. * If the request fails, the response content type will be `application/json`. Please refer to the failure codes in Responses section below. * If the query is executed successfully, the response content type will be `text/event-stream`. **For SSE** There are 3 types of data that will be sent to SSE channel 1. Query (type `query`): The first event of the result will ALWAYS be this type. 2. Metrics (type `metrics`): The query metrics in JSON. They will be sent every 1 seconds. 3. Data (the type is empty): The query result.

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
api_instance = swagger_client.QueriesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateQueryRequestV1Beta2() # CreateQueryRequestV1Beta2 | query request parameters

try:
    # execute a query and return the results
    api_response = api_instance.v1beta2_queries_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta2Api->v1beta2_queries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateQueryRequestV1Beta2**](CreateQueryRequestV1Beta2.md)| query request parameters | 

### Return type

[**Query**](Query.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_sqlanalyze_post**
> SQLAnalyzeResult v1beta2_sqlanalyze_post(body)

analyze sql

analyze sql

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
api_instance = swagger_client.QueriesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.AnalyzeSQLRequest() # AnalyzeSQLRequest | sql request parameters

try:
    # analyze sql
    api_response = api_instance.v1beta2_sqlanalyze_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueriesV1beta2Api->v1beta2_sqlanalyze_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyzeSQLRequest**](AnalyzeSQLRequest.md)| sql request parameters | 

### Return type

[**SQLAnalyzeResult**](SQLAnalyzeResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

