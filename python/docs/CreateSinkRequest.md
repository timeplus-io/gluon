# CreateSinkRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** | Sink name should only contain a maximum of 64 letters, numbers, or _, and start with a letter | 
**properties** | **dict(str, object)** | Additional properties that required to write the data to the sink (e.g. broker url). Please refer to the documentation for this sink type | [optional] 
**query** | **str** |  | [optional] 
**sql** | **str** | Deprecated. Use &#x60;query&#x60; instead. | [optional] 
**type** | **str** | Available types: [&#x60;slack&#x60;, &#x60;http&#x60;, &#x60;kafka&#x60;, &#x60;redpanda&#x60;, &#x60;confluent_cloud&#x60;, &#x60;pulsar&#x60;, &#x60;timeplus&#x60;]. Additional configurations such as broker url and etc. should be passed through &#x60;properties&#x60; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

