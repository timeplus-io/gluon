# StreamDef

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**list[ColumnDef]**](ColumnDef.md) |  | [optional] 
**description** | **str** |  | [optional] 
**event_time_column** | **str** | This column will be used as the event time if specified | [optional] 
**event_time_timezone** | **str** | The timezone of the &#x60;TimestampColumn&#x60; | [optional] 
**logstore_retention_bytes** | **int** | The max size a stream can grow. Defaulted to 10 GiB | [optional] 
**logstore_retention_ms** | **int** | The max time the data can be retained in the stream. Defaulted to 7 days | [optional] 
**mode** | **str** | Storage mode of stream. Possible values: &#x60;append&#x60;, &#x60;changelog&#x60;, &#x60;changelog_kv&#x60;, &#x60;versioned_kv&#x60; | [optional] 
**name** | **str** | Stream name should only contain a maximum of 64 letters, numbers, or _, and start with a letter | 
**order_by_expression** | **str** |  | [optional] 
**order_by_granularity** | **str** |  | [optional] 
**partition_by_granularity** | **str** |  | [optional] 
**primary_key** | **str** | Expression of primary key, required in &#x60;changelog_kv&#x60;&#x60; and &#x60;versioned_kv&#x60;&#x60; mode | [optional] 
**replication_factor** | **int** |  | [optional] 
**shards** | **int** |  | [optional] 
**ttl_expression** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

