"""
This script defines pytest fixtures for managing the testing environment.

- **pytest_addoption:** Adds a command-line option `--env` to specify the environment.
- **env_cli:** Retrieves the environment name provided with the `--env` option.
- **environment:** Determines the testing environment using a prioritized order:
    1. Command-line option `--env`
    2. Environment variable `ENV`
    3. Default value "dev"
- **api_config:** Creates an `ApiConfig` instance configured for the specified environment.
"""

import pytest
import os
from utils.config import ApiConfig
import logging

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    """
    Adds a command-line option `--env` to specify the environment files to use.

    Args:
        parser: The pytest argument parser.
    """

    parser.addoption(
        "--env",
        action="store",
        help="Indicates which environment files to use (e.g., --env=dev)",
    )


@pytest.fixture(scope='session')
def env_cli(request):
    """
    Retrieves the environment name provided with the `--env` command-line option.

    Args:
        request: The pytest request object.

    Returns:
        The environment name from the `--env` option, or None if not provided.
    """

    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def environment(env_cli):
    """
    Retrieves the environment from the `ENV` environment variable,
    the command-line argument `env_cli`, or uses 'dev' by default.

    Args:
        env_cli: The environment name potentially provided as a command-line argument.

    Returns:
        The determined environment name as a string.
    """

    env_var: str = os.environ.get("ENV")

    logger.debug(f"Environment from environment variable: {env_var}")
    logger.debug(f"Environment from command line argument: {env_cli}")

    env = env_cli or env_var or "dev"

    logger.debug(f"Selected environment: {env}")

    yield env


@pytest.fixture(scope='session')
def api_config(environment: str) -> ApiConfig:
    """
    Creates an instance of the `ApiConfig` class for the specified environment.

    Args:
        environment: The determined environment name from other fixtures.

    Returns:
        An instance of the `ApiConfig` class configured for the given environment.
    """

    return ApiConfig(environment)
