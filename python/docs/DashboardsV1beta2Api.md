# swagger_client.DashboardsV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_dashboards_get**](DashboardsV1beta2Api.md#v1beta2_dashboards_get) | **GET** /v1beta2/dashboards | list dashboards.
[**v1beta2_dashboards_id_delete**](DashboardsV1beta2Api.md#v1beta2_dashboards_id_delete) | **DELETE** /v1beta2/dashboards/{id} | delete a dashboard.
[**v1beta2_dashboards_id_get**](DashboardsV1beta2Api.md#v1beta2_dashboards_id_get) | **GET** /v1beta2/dashboards/{id} | get a dashboard.
[**v1beta2_dashboards_id_put**](DashboardsV1beta2Api.md#v1beta2_dashboards_id_put) | **PUT** /v1beta2/dashboards/{id} | Update a dashboard.
[**v1beta2_dashboards_post**](DashboardsV1beta2Api.md#v1beta2_dashboards_post) | **POST** /v1beta2/dashboards | create a dashboard.

# **v1beta2_dashboards_get**
> list[DashboardDashboard] v1beta2_dashboards_get()

list dashboards.

Get all dashboards.

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
api_instance = swagger_client.DashboardsV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list dashboards.
    api_response = api_instance.v1beta2_dashboards_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsV1beta2Api->v1beta2_dashboards_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DashboardDashboard]**](DashboardDashboard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_dashboards_id_delete**
> v1beta2_dashboards_id_delete(id)

delete a dashboard.

Delete the dashboard with the given ID.

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
api_instance = swagger_client.DashboardsV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | dashboard ID

try:
    # delete a dashboard.
    api_instance.v1beta2_dashboards_id_delete(id)
except ApiException as e:
    print("Exception when calling DashboardsV1beta2Api->v1beta2_dashboards_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| dashboard ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_dashboards_id_get**
> DashboardDashboard v1beta2_dashboards_id_get(id)

get a dashboard.

get a dashboard.

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
api_instance = swagger_client.DashboardsV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | dashboard ID

try:
    # get a dashboard.
    api_response = api_instance.v1beta2_dashboards_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsV1beta2Api->v1beta2_dashboards_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| dashboard ID | 

### Return type

[**DashboardDashboard**](DashboardDashboard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_dashboards_id_put**
> DashboardDashboard v1beta2_dashboards_id_put(body, id)

Update a dashboard.

Update the specific dashboard with the given ID.

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
api_instance = swagger_client.DashboardsV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateDashboardRequest() # UpdateDashboardRequest | update dashboard request parameters
id = 'id_example' # str | dashboard ID

try:
    # Update a dashboard.
    api_response = api_instance.v1beta2_dashboards_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsV1beta2Api->v1beta2_dashboards_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDashboardRequest**](UpdateDashboardRequest.md)| update dashboard request parameters | 
 **id** | **str**| dashboard ID | 

### Return type

[**DashboardDashboard**](DashboardDashboard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_dashboards_post**
> DashboardDashboard v1beta2_dashboards_post(body)

create a dashboard.

create a dashboard.

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
api_instance = swagger_client.DashboardsV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.CreateDashboardRequest() # CreateDashboardRequest | dashboard request parameters

try:
    # create a dashboard.
    api_response = api_instance.v1beta2_dashboards_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsV1beta2Api->v1beta2_dashboards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDashboardRequest**](CreateDashboardRequest.md)| dashboard request parameters | 

### Return type

[**DashboardDashboard**](DashboardDashboard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

