# CreateSourceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** | Source name should only contain a maximum of 64 letters, numbers, or _, and start with a letter | 
**properties** | **dict(str, object)** | Additional properties that required to read the data from source (e.g. broker url). Please refer to the documentation for this source type | [optional] 
**stream** | **str** | The name of the target stream that this source writes to. The stream needs to be created first. | 
**type** | **str** | Available types: [&#x60;ably&#x60;, &#x60;stream_generator&#x60;, &#x60;kafka&#x60;, &#x60;redpanda&#x60;, &#x60;confluent_cloud&#x60;, &#x60;pulsar&#x60;, &#x60;websocket&#x60;, &#x60;nats&#x60;, &#x60;nats_jetstream&#x60;]. Additional configurations such as broker url and etc. should be passed through &#x60;properties&#x60; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

