# UDF

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | [**list[UDFArgument]**](UDFArgument.md) | The input argument of the UDF   * For UDA: the number and type of arguments should be consistent with the main function of UDA.     the type should be the data types of proton not javascript types. It only supports int8/16/32/64, uint8/16/32/64, | [optional] 
**auth_context** | [**UDFAuthContext**](UDFAuthContext.md) |  | [optional] 
**auth_method** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | [**Owner**](Owner.md) |  | [optional] 
**description** | **str** |  | [optional] 
**is_aggregation** | **bool** | Whether it is an aggregation function. Only valid when type is &#x27;javascript&#x27; | [optional] 
**last_updated_at** | **str** |  | [optional] 
**last_updated_by** | [**Owner**](Owner.md) |  | [optional] 
**name** | **str** |  | [optional] 
**return_type** | **str** | The erturn type of the UDF   * For UDA: if it returns a single value, the return type is the corresponding data type of Timeplus.     It supports the same types of input arguments, except for datetime, it only supports DateTime64(3). | [optional] 
**source** | **str** | The source code of the UDA. There are functions to be defined:  * main function: with the same name as UDA. Timeplus calls this function for each input row. The main function can return two types of result: object or simple data type    - If it returns an object, the object is like {“emit”: true, “result”: …}. ‘Emit’ (boolean) property tells Timeplus whether or not the result should emit. ‘result’ is the current aggregate result, if ‘emit’ is false, the result will be ignored by Timeplus. Timeplus will convert the ‘result’ property of v8 to the data types defined when creating UDA.    - If it returns a simple data type, Timeplus considers the return data as the result to be emitted immediately. It converts the return data to the corresponding data type and Timeplus emits the aggregating result.    - Once UDA tells Timeplus to emit the data, UDA takes the full responsibility to clear the internal state, prepare and restart a new aggregating window, et al.  * state function: which returns the serialized state of all internal states of UDA in string. The UDA takes the responsibility therefore Timeplus can choose to persist the internal state of UDA for query recovery.  * init function: the input of this function is the string of serialized state of the internal states UDA. Timeplus calls this function when it wants to recover the aggregation function with the persisted internal state. | [optional] 
**type** | **str** | Either &#x60;javascript&#x60; or &#x60;remote&#x60; | [optional] 
**url** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

