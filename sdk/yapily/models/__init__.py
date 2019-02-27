# coding: utf-8

# flake8: noqa
"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.87
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from yapily.models.atm_branch import ATMBranch
from yapily.models.atm_geo_location import ATMGeoLocation
from yapily.models.atm_geographic_coordinates import ATMGeographicCoordinates
from yapily.models.atm_location import ATMLocation
from yapily.models.atm_location_other_location_category import ATMLocationOtherLocationCategory
from yapily.models.atm_map_service_links import ATMMapServiceLinks
from yapily.models.atm_open_data import ATMOpenData
from yapily.models.atm_open_data_atm import ATMOpenDataATM
from yapily.models.atm_open_data_brand import ATMOpenDataBrand
from yapily.models.atm_open_data_other_atm_services import ATMOpenDataOtherATMServices
from yapily.models.atm_open_data_other_accessibility import ATMOpenDataOtherAccessibility
from yapily.models.atm_open_data_response import ATMOpenDataResponse
from yapily.models.atm_postal_address import ATMPostalAddress
from yapily.models.atm_site import ATMSite
from yapily.models.account import Account
from yapily.models.account_authorisation_request import AccountAuthorisationRequest
from yapily.models.account_request import AccountRequest
from yapily.models.address import Address
from yapily.models.age_eligibility import AgeEligibility
from yapily.models.api_list_response_of_account import ApiListResponseOfAccount
from yapily.models.api_list_response_of_feature_details import ApiListResponseOfFeatureDetails
from yapily.models.api_list_response_of_institution import ApiListResponseOfInstitution
from yapily.models.api_list_response_of_transaction import ApiListResponseOfTransaction
from yapily.models.api_response_of_account import ApiResponseOfAccount
from yapily.models.api_response_of_authorisation_request_response import ApiResponseOfAuthorisationRequestResponse
from yapily.models.api_response_of_consent import ApiResponseOfConsent
from yapily.models.api_response_of_identity import ApiResponseOfIdentity
from yapily.models.api_response_of_list_of_atm_open_data_response import ApiResponseOfListOfATMOpenDataResponse
from yapily.models.api_response_of_list_of_personal_current_account_data import ApiResponseOfListOfPersonalCurrentAccountData
from yapily.models.api_response_of_payment_response import ApiResponseOfPaymentResponse
from yapily.models.api_response_of_transfer_response import ApiResponseOfTransferResponse
from yapily.models.application import Application
from yapily.models.application_user import ApplicationUser
from yapily.models.authorisation_request_response import AuthorisationRequestResponse
from yapily.models.consent import Consent
from yapily.models.core_product import CoreProduct
from yapily.models.country import Country
from yapily.models.create_consent_access_token import CreateConsentAccessToken
from yapily.models.credit_check import CreditCheck
from yapily.models.credit_interest import CreditInterest
from yapily.models.credit_interest_credit_interest_eligibility import CreditInterestCreditInterestEligibility
from yapily.models.credit_interest_tier_band import CreditInterestTierBand
from yapily.models.credit_interest_tier_band_set import CreditInterestTierBandSet
from yapily.models.eligibility import Eligibility
from yapily.models.eligibility_other_eligibility import EligibilityOtherEligibility
from yapily.models.feature_details import FeatureDetails
from yapily.models.filter_and_sort import FilterAndSort
from yapily.models.id_verification_check import IDVerificationCheck
from yapily.models.identity import Identity
from yapily.models.identity_address import IdentityAddress
from yapily.models.institution import Institution
from yapily.models.institution_consent import InstitutionConsent
from yapily.models.media import Media
from yapily.models.merchant import Merchant
from yapily.models.merchant_info import MerchantInfo
from yapily.models.new_application_user import NewApplicationUser
from yapily.models.next import Next
from yapily.models.other_application_frequency import OtherApplicationFrequency
from yapily.models.other_bank_interest_type import OtherBankInterestType
from yapily.models.other_calculation_frequency import OtherCalculationFrequency
from yapily.models.other_fee_rate_type import OtherFeeRateType
from yapily.models.other_fee_type import OtherFeeType
from yapily.models.other_residency_type import OtherResidencyType
from yapily.models.other_type import OtherType
from yapily.models.overdraft import Overdraft
from yapily.models.overdraft_fee_applicable_range import OverdraftFeeApplicableRange
from yapily.models.overdraft_other_fee_type import OverdraftOtherFeeType
from yapily.models.overdraft_overdraft_fee_charge_cap import OverdraftOverdraftFeeChargeCap
from yapily.models.overdraft_overdraft_fee_charge_detail import OverdraftOverdraftFeeChargeDetail
from yapily.models.overdraft_overdraft_fees_charges import OverdraftOverdraftFeesCharges
from yapily.models.overdraft_overdraft_fees_charges1 import OverdraftOverdraftFeesCharges1
from yapily.models.overdraft_overdraft_tier_band import OverdraftOverdraftTierBand
from yapily.models.overdraft_overdraft_tier_band_set import OverdraftOverdraftTierBandSet
from yapily.models.pagination import Pagination
from yapily.models.payment_response import PaymentResponse
from yapily.models.personal_current_account_brand import PersonalCurrentAccountBrand
from yapily.models.personal_current_account_data import PersonalCurrentAccountData
from yapily.models.personal_current_account_pca import PersonalCurrentAccountPCA
from yapily.models.personal_current_account_pca_marketing_state import PersonalCurrentAccountPCAMarketingState
from yapily.models.residency_eligibility import ResidencyEligibility
from yapily.models.response_entity import ResponseEntity
from yapily.models.response_list_meta import ResponseListMeta
from yapily.models.response_meta import ResponseMeta
from yapily.models.sort_code_payment_auth_request import SortCodePaymentAuthRequest
from yapily.models.sort_code_payment_request import SortCodePaymentRequest
from yapily.models.transaction import Transaction
from yapily.models.transfer_request import TransferRequest
from yapily.models.transfer_response import TransferResponse
from yapily.models.yapily_access_token import YapilyAccessToken
