# swagger_client.InvitationsV1beta2Api

All URIs are relative to *//us.timeplus.cloud/{workspace-id}/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1beta2_invitations_get**](InvitationsV1beta2Api.md#v1beta2_invitations_get) | **GET** /v1beta2/invitations | list invitations
[**v1beta2_invitations_id_delete**](InvitationsV1beta2Api.md#v1beta2_invitations_id_delete) | **DELETE** /v1beta2/invitations/{id} | delete an invitation
[**v1beta2_invitations_post**](InvitationsV1beta2Api.md#v1beta2_invitations_post) | **POST** /v1beta2/invitations | create an invitation

# **v1beta2_invitations_get**
> list[Invitation] v1beta2_invitations_get()

list invitations

Get all invitations.

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
api_instance = swagger_client.InvitationsV1beta2Api(swagger_client.ApiClient(configuration))

try:
    # list invitations
    api_response = api_instance.v1beta2_invitations_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsV1beta2Api->v1beta2_invitations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Invitation]**](Invitation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_invitations_id_delete**
> v1beta2_invitations_id_delete(id)

delete an invitation

Delete the invitation with the given ID. Deleting the invitation will remove the user from current workspace.

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
api_instance = swagger_client.InvitationsV1beta2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | invitation ID

try:
    # delete an invitation
    api_instance.v1beta2_invitations_id_delete(id)
except ApiException as e:
    print("Exception when calling InvitationsV1beta2Api->v1beta2_invitations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| invitation ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1beta2_invitations_post**
> v1beta2_invitations_post(body)

create an invitation

Invite an user to the current tenant.

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
api_instance = swagger_client.InvitationsV1beta2Api(swagger_client.ApiClient(configuration))
body = swagger_client.InvitationRequest() # InvitationRequest | create invitation request parameters

try:
    # create an invitation
    api_instance.v1beta2_invitations_post(body)
except ApiException as e:
    print("Exception when calling InvitationsV1beta2Api->v1beta2_invitations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvitationRequest**](InvitationRequest.md)| create invitation request parameters | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

