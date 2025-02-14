# PaymentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**payment_idempotency_id** | **str** |  | [optional] 
**institution_consent_id** | **str** |  | [optional] 
**payment_lifecycle_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_details** | [**PaymentStatusDetails**](PaymentStatusDetails.md) |  | [optional] 
**payee_details** | [**Payee**](Payee.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**amount_details** | [**Amount**](Amount.md) |  | [optional] 
**first_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**first_payment_date_time** | **datetime** |  | [optional] 
**next_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**next_payment_date_time** | **datetime** |  | [optional] 
**final_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**final_payment_date_time** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**previous_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**previous_payment_date_time** | **datetime** |  | [optional] 
**charge_details** | [**list[ChargeDetails]**](ChargeDetails.md) |  | [optional] 
**scheduled_payment_type** | **str** |  | [optional] 
**scheduled_payment_date_time** | **datetime** |  | [optional] 
**frequency** | [**FrequencyResponse**](FrequencyResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


