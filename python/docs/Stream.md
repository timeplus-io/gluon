# Stream

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**list[ColumnsResp]**](ColumnsResp.md) |  | 
**created_at** | **str** |  | [optional] 
**created_by** | [**Owner**](Owner.md) |  | [optional] 
**description** | **str** |  | 
**engine** | **str** |  | 
**is_external** | **bool** | Deprecated. | [optional] 
**last_updated_at** | **str** |  | [optional] 
**last_updated_by** | [**Owner**](Owner.md) |  | [optional] 
**logstore_retention_bytes** | **int** | The max size a stream can grow. Any non-positive value means unlimited size. | 
**logstore_retention_ms** | **int** | The max time the data can be retained in the stream. Any non-positive value means unlimited time. | 
**mode** | **str** | Storage mode of stream. Defaulted to &#x60;append&#x60;. | 
**name** | **str** |  | 
**primary_key** | **str** | Expression of primary key, required in &#x60;changelog_kv&#x60; and &#x60;versioned_kv&#x60; mode | [optional] 
**ttl** | **str** | Deprecated. Use &#x60;ttl_expression&#x60; instaed | 
**ttl_expression** | **str** | ORDER_BY     string        &#x60;json:\&quot;order_by_expression\&quot;&#x60; PATTITION_BY string        &#x60;json:\&quot;partition_by_expression\&quot;&#x60; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

