"""
These are tests for the JSONReader class.
"""

import os, json
import unittest
from json_loader import JSONReader

class JSONReaderTest(unittest.TestCase):
    def setUp(self):
        """
        Sets the default directory for test data and test schema
        """
        self.input_file_path = 'src/tests/data'
        self.destination_file_path = 'src/tests/schema'
        self.processor = JSONReader(self.input_file_path, self.destination_file_path)

    def tearDown(self):
        """
        Clears the output after each test
        """
        for file_path in os.listdir(self.destination_file_path):
            file_name = os.path.join(self.destination_file_path, file_path)
            os.remove(file_name)

    
    def test_load_json(self):
        """
        Tests the load_json method
        """
        file_path = os.path.join(self.input_file_path, 'data1.json')
        data = self.processor.load_json(file_path)

        loaded_json = {
           "participantIds": [
                "ABCDEFGHIJKLMNOPQRST",
                "ABCDEFGHIJKLMNOPQRSTUVWXY"
            ]
        }
        self.assertEqual(data, loaded_json)

    def test_process_json(self):
        """
        Tests the process_json method
        """
        file_path = os.path.join(self.input_file_path, 'data1.json')
        data = self.processor.load_json(file_path)
        schema = self.processor.process_json(data)

        expected_schema = {
             "participantIds": {
                "type": "ENUM",
                "values": "",
                "tag": "",
                "description": "",
                "required": False
            }
        }

        self.assertEqual(schema, expected_schema)

    def test_process_json_files(self):
        """
        Tests the process_json_files method.
        """
        self.processor.process_json_files()

        for file_name in os.listdir(self.destination_file_path):
            file_path = os.path.join(self.destination_file_path, file_name)
            with open(file_path, 'r') as file:
                schema = json.load(file)
            expected_schema_file = os.path.join('src/tests/schema', file_name)

            with open(expected_schema_file, 'r') as file:
                expected_schema = json.load(file)
            self.assertEqual(schema, expected_schema)


if __name__ == "__main__":
    unittest.main()

