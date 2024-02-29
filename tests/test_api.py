import requests

# from utils.config import ApiConfig
import logging

logger = logging.getLogger(__name__)
# logger.basicConfig(level=logging.DEBUG)
logger.debug("Test API Endpoint")


def test_api_endpoint(api_config):
    """
    Tests the `/api/v1/users` endpoint of the API.

    Args:
        api_config: The `ApiConfig` instance for the environment.

    Returns:
        None.
    """
    logger.info("Starting test_api_endpoint")

    base_url: str = api_config.base_url
    endpoint: str = "/people/1/"

    logger.debug(base_url)
    logger.debug(endpoint)

    response: requests.Response = requests.get(f"{base_url}{endpoint}")
    # response: requests.Response = requests.get("https://swapi.dev/api/people/1/")

    assert response.status_code == 200
