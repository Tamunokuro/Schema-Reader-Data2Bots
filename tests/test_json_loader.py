"""
These are tests for the JSONReader class.
"""

import os, json
import unittest
from json_reader.json_loader import JSONReader


class JSONReaderTest(unittest.TestCase):
    def setUp(self):
        """
        Sets the default directory for test data and test schema
        """
        self.input_file_path = "tests/data"
        self.destination_file_path = "tests/schema"
        self.reader = JSONReader(self.input_file_path, self.destination_file_path)

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
        file_path = os.path.join(self.input_file_path, "data1.json")
        data = self.reader.load_json(file_path)

        loaded_json = {
            "message": {
                "participantIds": ["ABCDEFGHIJKLMNOPQRST", "ABCDEFGHIJKLMNOPQRSTUVWXY"],
                "joiner": {
                    "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZAB",
                    "nickname": "ABCDEFGHIJKLMNO",
                    "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZABC",
                },
                "nations": "Gen-Z",
                "age": 27,
                "categories": [{"X-Men": "Marvel", "Justice League": "DC"}],
            }
        }
        self.assertEqual(data, loaded_json)

    def test_process_json(self):
        """
        Tests the process_json method
        """
        file_path = os.path.join(self.input_file_path, "data1.json")
        data = self.reader.load_json(file_path)
        schema_data = self.reader.process_json(data)

        expected_schema = {
            "participantIds": {
                "type": "ENUM",
                "values": "",
                "tag": "",
                "description": "",
                "required": False,
            },
            "joiner": {
                "type": "OBJECT",
                "tag": "",
                "description": "",
                "required": False,
            },
            "nations": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False,
            },
            "age": {"type": "INTEGER", "tag": "", "description": "", "required": False},
            "categories": {
                "type": "OBJECT",
                "tag": "",
                "description": "",
                "required": False,
            },
        }

        self.assertEqual(schema_data, expected_schema)

if __name__ == "__main__":
    unittest.main()
