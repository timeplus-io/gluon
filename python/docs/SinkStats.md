# SinkStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earliest_event** | **str** |  | [optional] 
**errors** | [**list[StatsError]**](StatsError.md) | It only contains the latest error of the pipeline | 
**failure_count** | **float** |  | 
**historical_data_bytes** | **int** |  | [optional] 
**latest_event** | **str** |  | [optional] 
**row_count** | **int** |  | [optional] 
**streaming_data_bytes** | **int** |  | [optional] 
**success_count** | **float** |  | 
**throughput** | [**list[StatsThroughput]**](StatsThroughput.md) | Each data point represents the average throughput for one minute | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

