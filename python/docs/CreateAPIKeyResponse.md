# CreateAPIKeyResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | generated API key. API keys are treated as secrets and are not stored in the system. It is the users&#x27; responsibility to safely store the API key for future use. | [optional] 
**created_at** | **int** | creation time represented as the number of seconds elapsed since January 1, 1970 UTC | [optional] 
**expire_at** | **int** | expiration time represented as the number of seconds elapsed since January 1, 1970 UTC | [optional] 
**id** | **str** | a string that identifies an API key, readonly. | [optional] 
**name** | **str** | the name of the API key | [optional] 
**permissions** | **list[str]** | list of permissions associated with the API key | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

