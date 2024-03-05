import logging
import random
import requests
import pytest

from utils.validate_schema import ValidateSchema
from utils.api_client import ApiClient
from ratelimit import limits, sleep_and_retry
from utils.generator import Generator

logger = logging.getLogger(__name__)
cp_generator : Generator = Generator(5, False)

@pytest.mark.parametrize("postal_code", cp_generator.postal_codes_list, ids=cp_generator.postal_codes_with_ids)
def test_az_gse_endpoint(api_config, postal_code):
    """
    Tests the `/GetBrokerDetails` endpoint with different postal codes.

    Args:
        api_config (ApiConfig): The API configuration object.
        postal_code (str): The postal code to use in the request.
    """

    # Create the API client
    api_client = ApiClient(api_config.az_gse_base_url,0,1)

    endpoint = "/GetBrokerDetails"
    params = {
        "postal_code": postal_code,
        "broker_id": "NULL",
        "product_code": "NULL",
        "search_type": "Broker",
        "lang_code": "FR",
        "country_code": "BE"
    }

    logger.debug(f"Testing AZ GSE endpoint with postal code: {postal_code}")

    response = api_client.get(endpoint, params=params)

    assert response.status_code == 200

def test_az_gse_valid_schema_getpostalcodes(api_config):
    """
    Tests if the response from the `/GetPotalCodes` endpoint matches the expected schema.

    Args:
        api_config (ApiConfig): The API configuration object.
    """
  
    logger.info(f"Testing AZ GSE schema : /getpostalcodes")

    # Create the API client
    api_client = ApiClient(api_config.az_gse_base_url)

    endpoint = "/GetPostalCodes"
    params = {
        "postal_code": "1000"
        #"broker_id": "NULL",
        #"product_code": "NULL",
        #"search_type": "Broker",
        #"lang_code": "FR",
        #"country_code": "BE"
    }

    response = response = api_client.get(endpoint, params=params).json()
    
    is_valid, message = ValidateSchema(schema_file=api_config.az_gse_getpostalcodes_schema).validate_json(response)

    logger.debug(f"Schema validation: {is_valid}")
    logger.debug(f"Validation message: {message}")

    assert is_valid

def test_az_gse_valid_schema_getproduct(api_config):
    """
    Tests if the response from the `/GetBrokerProducts` endpoint matches the expected schema.

    Args:
        api_config (ApiConfig): The API configuration object.
    """
  
    logger.info(f"Testing AZ GSE schema /GetBrokerProducts`")

    # Create the API client
    api_client = ApiClient(api_config.az_gse_base_url)

    endpoint = "/GetBrokerProducts"
    

    response = response = api_client.get(endpoint).json()
    
    is_valid, message = ValidateSchema(schema_file=api_config.az_gse_getproduct_schema).validate_json(response)

    logger.debug(f"Schema validation: {is_valid}")
    logger.debug(f"Validation message: {message}")

    assert is_valid

def test_az_gse_valid_schema_getbrokerdetails(api_config):
    """
    Tests if the response from the `/GetBrokerDetails` endpoint matches the expected schema.

    Args:
        api_config (ApiConfig): The API configuration object.
    """
  
    logger.info(f"Testing AZ GSE schema : /getbrokerdetails")

    # Create the API client
    api_client = ApiClient(api_config.az_gse_base_url)

    endpoint = "/GetBrokerDetails"
    params = {
        "postal_code": "1000",
        "broker_id": "NULL",
        "product_code": "NULL",
        "search_type": "Broker",
        "lang_code": "FR",
        "country_code": "BE"
    }

    response = response = api_client.get(endpoint, params=params).json()
    
    is_valid, message = ValidateSchema(schema_file=api_config.az_gse_base_schema).validate_json(response)

    logger.debug(f"Schema validation: {is_valid}")
    logger.debug(f"Validation message: {message}")

    assert is_valid
