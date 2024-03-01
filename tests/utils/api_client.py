from typing import Optional, Union, Tuple

from ratelimit import limits
import requests
import time


class ApiClient:
    """
    Generic API client class with rate limiting and sleep functionality.

    Args:
        base_url (str): The base URL of the API.
        rate_limit (Optional[Tuple[int, str]], optional): Rate limit configuration (e.g., (1, "1s") for 1 request per second).
        sleep_time (float, optional): Delay between requests (in seconds).
    """

    def __init__(self, base_url: str, rate_limit: int = 0, sleep_time: float = 0):
        self.base_url: str = base_url
        self.rate_limit: int = rate_limit
        self.sleep_time: float = sleep_time

        if self.rate_limit:
            self._limiter = limits(*self.rate_limit)

    def _make_request(self, method: str, endpoint: str, data: Optional[dict] = None, params: Optional[dict] = None) -> requests.Response:
        """
        Sends a request to the API with rate limiting and sleep handling.

        Args:
            method (str): The HTTP method (GET, POST, etc.).
            endpoint (str): The API endpoint.
            data (dict, optional): The request data.

        Returns:
            requests.Response: The response object from the request.
        """

        if self.rate_limit:
            self._limiter.wait()

        if self.sleep_time:
            time.sleep(self.sleep_time)

        url: str = f"{self.base_url}{endpoint}"
        request_fn = getattr(requests, method.lower())
        response: requests.Response = request_fn(url, data=data, params=params)
        response.raise_for_status()
        return response

    def get(self, endpoint: str, params: Optional[dict] = None) -> requests.Response:
        """
        Sends a GET request to the API.

        Args:
            endpoint (str): The API endpoint.
            params (dict, optional): The request parameters.

        Returns:
            requests.Response: The response object from the request.
        """

        return self._make_request("GET", endpoint, params=params) # type: ignore

    def post(self, endpoint: str, data: Optional[dict] = None) -> requests.Response:
        """
        Sends a POST request to the API.

        Args:
            endpoint (str): The API endpoint.
            data (dict, optional): The request data.

        Returns:
            requests.Response: The response object from the request.
        """

        return self._make_request("POST", endpoint, data=data)