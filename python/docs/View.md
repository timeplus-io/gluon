# View

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**list[ColumnsResp]**](ColumnsResp.md) | The columns in the view | 
**created_at** | **str** |  | [optional] 
**created_by** | [**Owner**](Owner.md) |  | [optional] 
**description** | **str** |  | 
**last_updated_at** | **str** |  | [optional] 
**last_updated_by** | [**Owner**](Owner.md) |  | [optional] 
**logstore_retention_bytes** | **int** | Only avaialable for materialized view. The max size a materialized view can grow. Any non-positive value means unlimited size. | 
**logstore_retention_ms** | **int** | Only avaialable for materialized view. The max time the data can be retained in the materialized view. Any non-positive value means unlimited time. | 
**materialized** | **bool** |  | 
**name** | **str** |  | 
**query** | **str** |  | 
**target_stream** | **str** | This field is applicable for materialized view only. | 
**ttl** | **str** | Deprecated. Use &#x60;ttl_expression&#x60; instaed | 
**ttl_expression** | **str** | Only avaialable for materialized view | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

