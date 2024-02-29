import json
import jsonschema
from jsonschema import validate

class ValidateSchema:
    """Class for validating JSON data against a schema."""

    def __init__(self, schema_file="user_schema.json"):
        """
        Initializes the class with the schema file path.

        Args:
            schema_file (str, optional): Path to the JSON schema file.
                Defaults to "user_schema.json".
        """
        self.schema = self._load_schema(schema_file)

    def _load_schema(self, schema_file):
        """Loads the JSON schema from the specified file."""
        with open(schema_file, 'r') as file:
            return json.load(file)

    def validate_json(self, json_data):
        """Validates the JSON data against the loaded schema.

        Args:
            json_data (dict): The JSON data to validate.

        Returns:
            tuple: (bool, str) indicating validation success and message.
        """
        try:
            validate(instance=json_data, schema=self.schema)
            return True, "Given JSON data is Valid"
        except jsonschema.exceptions.ValidationError as err:
            return False, "Given JSON data is Invalid: {}".format(err)
