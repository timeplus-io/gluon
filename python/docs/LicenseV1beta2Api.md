# swagger_client.LicenseV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_licenses_get**](LicenseV1beta2Api.md#v1beta2_licenses_get) | **GET** /v1beta2/licenses | list all lcenses
[**v1beta2_licenses_id_delete**](LicenseV1beta2Api.md#v1beta2_licenses_id_delete) | **DELETE** /v1beta2/licenses/{id} | remove a lcense by id
[**v1beta2_licenses_id_get**](LicenseV1beta2Api.md#v1beta2_licenses_id_get) | **GET** /v1beta2/licenses/{id} | get a lcense by id
[**v1beta2_licenses_post**](LicenseV1beta2Api.md#v1beta2_licenses_post) | **POST** /v1beta2/licenses | upload and create a lcense

# **v1beta2_licenses_get**
> list[LicenseLicense] v1beta2_licenses_get()

list all lcenses

list all lcenses

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
api_instance = swagger_client.LicenseV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list all lcenses
    api_response = api_instance.v1beta2_licenses_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseV1beta2Api->v1beta2_licenses_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LicenseLicense]**](LicenseLicense.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_licenses_id_delete**
> LicenseLicense v1beta2_licenses_id_delete(id)

remove a lcense by id

remove a lcense by id

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
api_instance = swagger_client.LicenseV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | license ID

try:
    # remove a lcense by id
    api_response = api_instance.v1beta2_licenses_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseV1beta2Api->v1beta2_licenses_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| license ID | 

### Return type

[**LicenseLicense**](LicenseLicense.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_licenses_id_get**
> LicenseLicense v1beta2_licenses_id_get(id)

get a lcense by id

get a lcense by id

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
api_instance = swagger_client.LicenseV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | license ID

try:
    # get a lcense by id
    api_response = api_instance.v1beta2_licenses_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseV1beta2Api->v1beta2_licenses_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| license ID | 

### Return type

[**LicenseLicense**](LicenseLicense.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_licenses_post**
> LicenseLicense v1beta2_licenses_post(body)

upload and create a lcense

upload and create a lcense.

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
api_instance = swagger_client.LicenseV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.V1beta2LicensesBody() # V1beta2LicensesBody | 

try:
    # upload and create a lcense
    api_response = api_instance.v1beta2_licenses_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseV1beta2Api->v1beta2_licenses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta2LicensesBody**](V1beta2LicensesBody.md)|  | 

### Return type

[**LicenseLicense**](LicenseLicense.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

