# CreateViewRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**logstore_retention_bytes** | **int** | The max size a stream can grow. Any non-positive value means unlimited size. Defaulted to 10 GiB. | [optional] 
**logstore_retention_ms** | **int** | The max time the data can be retained in the stream. Any non-positive value means unlimited time. Defaulted to 7 days. | [optional] 
**materialized** | **bool** |  | [optional] [default to False]
**name** | **str** | View name should only contain a maximum of 64 letters, numbers, or _, and start with a letter | 
**query** | **str** |  | 
**target_stream** | **str** | This option is applicable only when &#x60;materialized&#x60; is &#x60;true&#x60;. Specify this when you want to have multiple materialized views sink to the same target stream. | [optional] 
**ttl_expression** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

