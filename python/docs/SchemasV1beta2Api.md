# swagger_client.SchemasV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_schemas_get**](SchemasV1beta2Api.md#v1beta2_schemas_get) | **GET** /v1beta2/schemas | list schemas
[**v1beta2_schemas_name_delete**](SchemasV1beta2Api.md#v1beta2_schemas_name_delete) | **DELETE** /v1beta2/schemas/{name} | delete a schema
[**v1beta2_schemas_name_get**](SchemasV1beta2Api.md#v1beta2_schemas_name_get) | **GET** /v1beta2/schemas/{name} | get a schema
[**v1beta2_schemas_name_put**](SchemasV1beta2Api.md#v1beta2_schemas_name_put) | **PUT** /v1beta2/schemas/{name} | update a schema
[**v1beta2_schemas_post**](SchemasV1beta2Api.md#v1beta2_schemas_post) | **POST** /v1beta2/schemas | create a schema

# **v1beta2_schemas_get**
> list[SchemaResp] v1beta2_schemas_get()

list schemas

Get all schemas.

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
api_instance = swagger_client.SchemasV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list schemas
    api_response = api_instance.v1beta2_schemas_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemasV1beta2Api->v1beta2_schemas_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SchemaResp]**](SchemaResp.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_schemas_name_delete**
> v1beta2_schemas_name_delete(name)

delete a schema

Delete the schema with the given name.

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
api_instance = swagger_client.SchemasV1beta2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | schema

try:
    # delete a schema
    api_instance.v1beta2_schemas_name_delete(name)
except ApiException as e:
    print("Exception when calling SchemasV1beta2Api->v1beta2_schemas_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| schema | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_schemas_name_get**
> SchemaResp v1beta2_schemas_name_get(name)

get a schema

get schema with the given name.

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
api_instance = swagger_client.SchemasV1beta2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | schema name

try:
    # get a schema
    api_response = api_instance.v1beta2_schemas_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemasV1beta2Api->v1beta2_schemas_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| schema name | 

### Return type

[**SchemaResp**](SchemaResp.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_schemas_name_put**
> V1beta2UpdateSchemaRequest v1beta2_schemas_name_put(body)

update a schema

Update the specific schema with the given content.

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
api_instance = swagger_client.SchemasV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.V1beta2UpdateSchemaRequest() # V1beta2UpdateSchemaRequest | update Schema request parameters

try:
    # update a schema
    api_response = api_instance.v1beta2_schemas_name_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemasV1beta2Api->v1beta2_schemas_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta2UpdateSchemaRequest**](V1beta2UpdateSchemaRequest.md)| update Schema request parameters | 

### Return type

[**V1beta2UpdateSchemaRequest**](V1beta2UpdateSchemaRequest.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_schemas_post**
> V1beta2CreateSchemaRequest v1beta2_schemas_post(body)

create a schema

Create a schema

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
api_instance = swagger_client.SchemasV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.V1beta2CreateSchemaRequest() # V1beta2CreateSchemaRequest | create Schema request parameters

try:
    # create a schema
    api_response = api_instance.v1beta2_schemas_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemasV1beta2Api->v1beta2_schemas_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta2CreateSchemaRequest**](V1beta2CreateSchemaRequest.md)| create Schema request parameters | 

### Return type

[**V1beta2CreateSchemaRequest**](V1beta2CreateSchemaRequest.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

