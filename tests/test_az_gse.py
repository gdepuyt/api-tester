import logging
import random
import requests
import pytest

from utils.validate_schema import ValidateSchema
from utils.api_client import ApiClient
from ratelimit import limits, sleep_and_retry

logger = logging.getLogger(__name__)


def _generate_random_postal_code_list(x):
  """
  Generates a random list of x postal between 1000 and 9992 (inclusive).

  Args:
      x (int): The number of elements in the desired list.

  Returns:
      list: A list of x random integers between 1000 and 9992.
  """

  return [random.randint(1000, 9992) for _ in range(x)]


@pytest.mark.parametrize("postal_code", _generate_random_postal_code_list(5))
def test_az_gse_endpoint(api_config, postal_code):
    """
    Tests the `/GetBrokerDetails` endpoint with different postal codes.

    Args:
        api_config (ApiConfig): The API configuration object.
        postal_code (str): The postal code to use in the request.
    """

    # Create the API client
    api_client = ApiClient(api_config.az_gse_base_url,0,5)

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

def test_az_gse_valid_schema(api_config):
    """
    Tests if the response from the `/GetBrokerDetails` endpoint matches the expected schema.

    Args:
        api_config (ApiConfig): The API configuration object.
    """
  
    logger.debug(f"Testing AZ GSE schema")

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
