import logging
import random
import requests
import pytest

from utils.validate_schema import ValidateSchema
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



RATE_LIMIT_WINDOW = 5  # Rate limit window (e.g., "1s" for one request per second)
RATE_LIMIT_LIMIT = 1  # Allowed requests within the window

@sleep_and_retry
@limits(calls=RATE_LIMIT_LIMIT, period=RATE_LIMIT_WINDOW) # type: ignore
def _send_request_with_ratelimit(url):
    """
    Sends a GET request to the provided URL with rate limiting.

    Args:
        url (str): The URL to send the request to.

    Returns:
        requests.Response: The response object from the request.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response


def _build_url(api_config, endpoint, postal_code):
    """
    Builds the complete URL considering the postal code.

    Args:
        api_config (ApiConfig): The API configuration object.
        endpoint (str): The API endpoint path.
        postal_code (str): The specific postal code for the request.

    Returns:
        str: The complete URL.
    """
    params = f"postal_code={postal_code}&broker_id=NULL&product_code=NULL&search_type=Broker&lang_code=FR&country_code=BE"
    return f"{api_config.az_gse_base_url}{endpoint}?{params}"


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


@pytest.mark.parametrize("postal_code", _generate_random_postal_code_list(2))
def test_az_gse_endpoint(api_config, postal_code):
    """
    Tests the `/GetBrokerDetails` endpoint with different postal codes.

    Args:
        api_config (ApiConfig): The API configuration object.
        postal_code (str): The postal code to use in the request.
    """
    endpoint = "/GetBrokerDetails"
    url = _build_url(api_config, endpoint, postal_code)

    logger.debug(f"Testing AZ GSE endpoint with postal code: {postal_code} - {url}")

    response = _send_request_with_ratelimit(url)

    assert response.status_code == 200

def test_az_gse_valid_schema(api_config):
    """
    Tests if the response from the `/GetBrokerDetails` endpoint matches the expected schema.

    Args:
        api_config (ApiConfig): The API configuration object.
    """
    endpoint = "/GetBrokerDetails"
    url = _build_url(api_config, endpoint, 1000)

    logger.debug(f"Testing AZ GSE schema: {url}")

    response = _send_request(url)
    response_dict = response.json()

    logger.debug(response.content)
    logger.debug(response_dict)

    is_valid, message = ValidateSchema(schema_file=api_config.az_gse_base_schema).validate_json(response_dict)

    logger.debug(f"Schema validation: {is_valid}")
    logger.debug(f"Validation message: {message}")

    assert is_valid