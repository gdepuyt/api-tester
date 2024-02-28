"""
Module `utils.config` for managing configuration files.

This module provides a class `ApiConfig` for reading environment-specific `.ini`
configuration files.

**Classes:**

- `ApiConfig`: Encapsulates reading environment-specific `.ini` configuration files.
"""

import configparser
import logging
import os

logger = logging.getLogger(__name__)
logger.debug("utils.config")


class ApiConfig:
    """
    Class to encapsulate reading configuration files.

    **Attributes:**

    - `env`: The name of the environment.
    - `config`: An instance of `configparser.ConfigParser`.
    """

    def __init__(self, env: str):
        """
        Initializes an instance of the `ApiConfig` class with the specified environment.

        Args:
            env: The name of the environment.

        Returns:
            None.
        """

        logger.debug(f"Path where code is executed: {os.getcwd()}")
        self.env: str = env
        self.config: configparser.ConfigParser = configparser.ConfigParser()
        self.config.read(f"config/{env}.ini")

    @property
    def base_url(self) -> str:
        """
        Returns the base URL of the API for the specified environment.

        Args:
            None.

        Returns:
            The base URL as a string.
        """
        
        return self.config["API"]["base_url"]
