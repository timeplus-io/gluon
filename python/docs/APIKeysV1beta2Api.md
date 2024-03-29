# swagger_client.APIKeysV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_auth_api_keys_get**](APIKeysV1beta2Api.md#v1beta2_auth_api_keys_get) | **GET** /v1beta2/auth/api_keys | list API keys
[**v1beta2_auth_api_keys_id_delete**](APIKeysV1beta2Api.md#v1beta2_auth_api_keys_id_delete) | **DELETE** /v1beta2/auth/api_keys/{id} | delete an API key
[**v1beta2_auth_api_keys_post**](APIKeysV1beta2Api.md#v1beta2_auth_api_keys_post) | **POST** /v1beta2/auth/api_keys | create an API key

# **v1beta2_auth_api_keys_get**
> list[APIKey] v1beta2_auth_api_keys_get()

list API keys

Get all API keys created by current user

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
api_instance = swagger_client.APIKeysV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list API keys
    api_response = api_instance.v1beta2_auth_api_keys_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysV1beta2Api->v1beta2_auth_api_keys_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[APIKey]**](APIKey.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_auth_api_keys_id_delete**
> v1beta2_auth_api_keys_id_delete(id)

delete an API key

Delete the API key with the givin ID

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
api_instance = swagger_client.APIKeysV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | API key ID

try:
    # delete an API key
    api_instance.v1beta2_auth_api_keys_id_delete(id)
except ApiException as e:
    print("Exception when calling APIKeysV1beta2Api->v1beta2_auth_api_keys_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| API key ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_auth_api_keys_post**
> CreateAPIKeyResponse v1beta2_auth_api_keys_post(body=body)

create an API key

Create a new API key with optional expiration, the created API key represents the owner thus has the same permissions as the owner

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
api_instance = swagger_client.APIKeysV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateAPIKeyRequest() # CreateAPIKeyRequest | API Key parameters (optional)

try:
    # create an API key
    api_response = api_instance.v1beta2_auth_api_keys_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysV1beta2Api->v1beta2_auth_api_keys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAPIKeyRequest**](CreateAPIKeyRequest.md)| API Key parameters | [optional] 

### Return type

[**CreateAPIKeyResponse**](CreateAPIKeyResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

