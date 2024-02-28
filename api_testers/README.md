## API Tester

**Description**

This Python project provides a framework for testing APIs using the Pytest library. It offers functionalities for:

* **Configuring different test environments:** Easily switch between development, staging, and production environments using configuration files.
* **Sending API requests and handling responses:** Make HTTP requests to your API endpoints and assert the expected responses.
* **Defining test cases and assertions:** Write clear and maintainable test cases using Pytest's features.
* **Logging test execution and results:** Track test execution details and results for better debugging and monitoring.

**Installation**

1. **Clone the repository:**

```bash
git clone https://github.com/gdepuyt/api-tester.git
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

**Usage**

1. **Configure the test environment:**

   * Edit the configuration files in the `config` directory to specify details like API base URLs
   * You can leverage environment variables (e.g., `ENV`) to activate different configurations.

2. **Run the tests:**

   ```bash
   pytest -s -v
   ```

**Structure**

```
api-tester/
├── conftest.py          # Pytest configuration and fixtures
├── test/
│   ├── api_tests.py      # API test cases
│   └── ...               # Other test files (optional)
├── utils/
│   ├── config.py        # Configuration logic and classes
│   └── __init__.py      # Empty file to mark the directory as a package
├── README.md            # This file
├── requirements.txt     # Project dependencies
└── pytest.ini           # Pytest configuration file
```

**Example Test**

```python
# test/api_tests.py
from utils.config import api_config

def test_api_endpoint():
    """
    Tests the `/api/v1/users` endpoint of the API.

    Args:
        api_config: The `ApiConfig` instance for the environment.

    Returns:
        None.
    """
    base_url: str = api_config.base_url
    endpoint: str = "/api/v1/users"
    response: requests.Response = requests.get(f"{base_url}{endpoint}")

    assert response.status_code == 200
```

