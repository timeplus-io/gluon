# CreateAPIKeyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expire_at** | **str** | define the expiration time of the API key by specifying the exact date time, cannot use with expire_in | [optional] 
**expire_in** | **str** | define the expiration time of the API key by specifying the amount of time to count from now, cannot use with expire_at | [optional] 
**name** | **str** | the name of the API key. * If name is speicfied, the masked API key will be appended to the end of the name (e.g. &#x60;myAPIKey (vthm****OjXG)&#x60;). * If name is not speicfied, the masked API key will be used as the name (e.g. &#x60;vthm****OjXG&#x60;). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

