# swagger_client.TopologyV1beta2Api

All URIs are relative to *https//beta.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_topology_get**](TopologyV1beta2Api.md#v1beta2_topology_get) | **GET** /v1beta2/topology | get topology graph.

# **v1beta2_topology_get**
> Graph v1beta2_topology_get()

get topology graph.

get topology graph.

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
api_instance = swagger_client.TopologyV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # get topology graph.
    api_response = api_instance.v1beta2_topology_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyV1beta2Api->v1beta2_topology_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Graph**](Graph.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

