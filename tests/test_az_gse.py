import logging
import random
import requests


from utils.schema_validator import ValidateSchema

logger = logging.getLogger(__name__)

import random

def _generate_random_postal_code_list(x):
  """
  Generates a random list of x postal between 1000 and 9992 (inclusive).

  Args:
      x (int): The number of elements in the desired list.

  Returns:
      list: A list of x random integers between 1000 and 9992.
  """

  return [random.randint(1000, 9992) for _ in range(x)]


def _build_url(api_config, endpoint):
    """
    Builds the complete URL using the base URL and endpoint.

    Args:
        api_config (ApiConfig): The API configuration object.
        endpoint (str): The API endpoint path.

    Returns:
        str: The complete URL.
    """
    return f"{api_config.az_gse_base_url}{endpoint}"


def _send_request(url):
    """
    Sends a GET request to the provided URL and returns the response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        requests.Response: The response object from the request.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return response


def test_az_gse_endpoint(api_config):
    """
    Tests the `/GetBrokerDetails` endpoint of the Allianz Generic Search Engine.

    Args:
        api_config (ApiConfig): The API configuration object.
    """
    endpoint = "/GetBrokerDetails?postal_code=1000&broker_id=NULL&product_code=NULL&search_type=Broker&lang_code=FR&country_code=BE"
    url = _build_url(api_config, endpoint)

    logger.debug(f"Testing AZ GSE endpoint: {url}")

    response = _send_request(url)

    assert response.status_code == 200


def test_az_gse_valid_schema(api_config):
    """
    Tests if the response from the `/GetBrokerDetails` endpoint matches the expected schema.

    Args:
        api_config (ApiConfig): The API configuration object.
    """
    endpoint = "/GetBrokerDetails?postal_code=1000&broker_id=NULL&product_code=NULL&search_type=Broker&lang_code=FR&country_code=BE"
    url = _build_url(api_config, endpoint)

    logger.debug(f"Testing AZ GSE schema: {url}")

    response = _send_request(url)
    response_dict = response.json()

    is_valid, message = ValidateSchema(schema_file=api_config.az_gse_base_schema).validate_json(response_dict)

    logger.debug(f"Schema validation: {is_valid}")
    logger.debug(f"Validation message: {message}")

    assert is_valid