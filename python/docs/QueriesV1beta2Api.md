# swagger_client.QueriesV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_queries_post**](QueriesV1beta2Api.md#v1beta2_queries_post) | **POST** /v1beta2/queries | execute a query and return the results.

# **v1beta2_queries_post**
> Query v1beta2_queries_post(body)

execute a query and return the results.

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
    # execute a query and return the results.
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

