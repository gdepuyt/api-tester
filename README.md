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

**Core Folders**

* **test/**: Contains all your API test case files. Here's where you'll write the Pytest code to define your API tests.
   * **api_tests.py**: A sample file demonstrating how to write basic API tests. You can add more test files as needed.

* **utils/**: Houses supporting utilities and helper code for your testing framework.
    * **config.py**: Handles configuration management, reading environment variables, and loading different configurations based on the environment.

**Essential Files**

* **conftest.py**: Provides Pytest fixtures and potentially additional configuration for your tests.  Fixtures are reusable bits of code used to set up the test environment or provide common test data.

* **README.md**: The project's documentation. Explains its purpose, usage instructions, structure, examples, and customization options.

* **requirements.txt**:  Lists all the Python packages and dependencies  required for the project to function correctly.

* **pytest.ini**: Configuration file for customizing Pytest's behavior and settings.

**How it all works together:**

1. You write your test cases in the `test` directory (such as within `api_tests.py`), making use of the `requests` library or other HTTP clients to interact with your API.

2. `utils/config.py` assists in managing different test environments (e.g., "dev," "stage," "prod") and loading appropriate API URLs, credentials, and other configuration details.

3. Fixtures defined in `conftest.py` can offer test setup and teardown functionality, potentially sharing resources across tests.

4. You execute the tests using the `pytest` command, which automatically discovers and runs your test cases, leveraging any configurations specified in your `pytest.ini` file.




**Structure**

```
.
├── README.md
├── config
│   ├── dev.ini
│   ├── prod.ini
│   ├── test.ini
│   └── uat.ini
├── pytest.ini
├── requirements.txt
├── src
└── tests
    ├── conftest.py
    ├── test_api.py
    └── utils
        ├── __init__.py
        └── config.py
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

**Reference - sources**

* https://docs.pytest.org/
* https://pytest-with-eric.com/configuration/pytest-config-file/#Getting-Started
* https://github.com/microsoft/vscode-python/issues/18821

