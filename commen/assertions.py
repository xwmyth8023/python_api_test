import json
from os.path import join, dirname
from jsonschema import validate

# class JsonResonseValidate():

#     def __init__(self):
#         self.filename = 'hbib1.json'

def _load_json_schema(filename):
    """ Loads the given schema file """

    relative_path = join('schemas',filename)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())

def assert_valid_schema(data,filename):
    """ Checks whether the given data matches the schema """

    schema = _load_json_schema(filename)
    return validate(data, schema)
