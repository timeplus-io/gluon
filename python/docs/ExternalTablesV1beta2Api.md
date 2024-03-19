# swagger_client.ExternalTablesV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_external_tables_get**](ExternalTablesV1beta2Api.md#v1beta2_external_tables_get) | **GET** /v1beta2/external_tables | list external tables
[**v1beta2_external_tables_name_delete**](ExternalTablesV1beta2Api.md#v1beta2_external_tables_name_delete) | **DELETE** /v1beta2/external_tables/{name} | delete an external table
[**v1beta2_external_tables_name_get**](ExternalTablesV1beta2Api.md#v1beta2_external_tables_name_get) | **GET** /v1beta2/external_tables/{name} | get an external table
[**v1beta2_external_tables_post**](ExternalTablesV1beta2Api.md#v1beta2_external_tables_post) | **POST** /v1beta2/external_tables | create an external table

# **v1beta2_external_tables_get**
> list[ExternalTable] v1beta2_external_tables_get()

list external tables

Get all external tables.

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
api_instance = swagger_client.ExternalTablesV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list external tables
    api_response = api_instance.v1beta2_external_tables_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalTablesV1beta2Api->v1beta2_external_tables_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ExternalTable]**](ExternalTable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_external_tables_name_delete**
> v1beta2_external_tables_name_delete(name)

delete an external table

Delete the external table with the given name.

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
api_instance = swagger_client.ExternalTablesV1beta2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | external table name

try:
    # delete an external table
    api_instance.v1beta2_external_tables_name_delete(name)
except ApiException as e:
    print("Exception when calling ExternalTablesV1beta2Api->v1beta2_external_tables_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| external table name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_external_tables_name_get**
> ExternalTable v1beta2_external_tables_name_get(name)

get an external table

Get the external table with the given name.

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
api_instance = swagger_client.ExternalTablesV1beta2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | external table name

try:
    # get an external table
    api_response = api_instance.v1beta2_external_tables_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalTablesV1beta2Api->v1beta2_external_tables_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| external table name | 

### Return type

[**ExternalTable**](ExternalTable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_external_tables_post**
> ExternalTableDef v1beta2_external_tables_post(body)

create an external table

Create an external table.

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
api_instance = swagger_client.ExternalTablesV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.ExternalTableDef() # ExternalTableDef | create external table request parameters

try:
    # create an external table
    api_response = api_instance.v1beta2_external_tables_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalTablesV1beta2Api->v1beta2_external_tables_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalTableDef**](ExternalTableDef.md)| create external table request parameters | 

### Return type

[**ExternalTableDef**](ExternalTableDef.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

