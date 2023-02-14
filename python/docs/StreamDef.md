# StreamDef

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**list[ColumnDef]**](ColumnDef.md) |  | [optional] 
**description** | **str** |  | [optional] 
**event_time_column** | **str** |  | [optional] 
**event_time_timezone** | **str** |  | [optional] 
**logstore_retention_bytes** | **int** |  | [optional] 
**logstore_retention_ms** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 
**name** | **str** | Stream name should only contain a maximum of 64 letters, numbers, or _, and start with a letter | 
**order_by_expression** | **str** |  | [optional] 
**order_by_granularity** | **str** |  | [optional] 
**partition_by_granularity** | **str** |  | [optional] 
**primary_key** | **str** |  | [optional] 
**replication_factor** | **int** |  | [optional] 
**shards** | **int** |  | [optional] 
**ttl_expression** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

