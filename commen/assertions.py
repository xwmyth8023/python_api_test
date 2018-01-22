import json
from os.path import join, dirname
from jsonschema import validate

class JsonResonseValidate():

    def __init__(self,filename):
        self.filename = filename

    def _load_json_schema(self):
        """ Loads the given schema file """

        relative_path = join('schemas',self.filename)
        absolute_path = join(dirname(__file__), relative_path)
        print (relative_path,absolute_path)

        with open(absolute_path) as schema_file:
            return json.loads(schema_file.read())

    def assert_valid_schema(self,data):
        """ Checks whether the given data matches the schema """

        schema = self._load_json_schema()
        return validate(data, schema)
