import os, json
from typing import Any, Dict, List, Union

JSONValue = Union[str, int, List[Any], Dict[str, Any]]
JSONSchema = Dict[str, Any]

class JSONReader:
    """
    This class takes two arguments, the path from which the data 
    is loaded from and the path
    to which the data is saved to.
    """
    def __init__(self, path: str, destination_path: str = '/schema/'):
        self.path = path
        self.destination_path = destination_path

    def load_json(self, path: str) -> Dict[str, Any]:
        with open(path, 'r') as json_data:
            data = json.load(json_data)
        return data
    
    def process_json(self, data: Dict[str, Any]) -> JSONSchema:
        # Capture message attribute from data
        message_attr = data.get('message', {})

        schema_output: JSONSchema = {}

        for key, value in message_attr.items():
            if isinstance(value, str):
                schema_output[key] = {
                    "type": "STRING",
                    "tag": "",
                    "description": "",
                    "required": False 
                } 
            elif isinstance(value, int):
                schema_output[key] = {
                    "type": "INTEGER",
                    "tag": "",
                    "description": "", 
                    "required": False
                }
            elif isinstance(value, dict) or all(isinstance(item, dict) for item in value):
                schema_output[key] = {
                    "tag": "",
                    "description": "",
                    "required": False,
                    "values": ""                }

            elif isinstance(value, list) and all(isinstance(item, str) for item in value):
                schema_output[key] = {
                    "type": "ENUM",
                    "values": "",
                    "tag": "",
                    "description": "",
                    "required": False
                }
            elif isinstance(value, list) and all(isinstance(item, dict) for item in value):
                schema_output[key] = {
                    "type": "ARRAY",
                    "items": "", 
                    "tag": "",
                    "description": "",
                    "required": False
                }
        return schema_output
    
    def write_to_file(self, schema: JSONSchema, filepath: str) -> None:
        
        padded_schema = {
            "tags": "",
            "description": "",
            **schema
        }

        with open(filepath, 'w') as file:
            json.dump(padded_schema, file, indent=4)

    def process_json_files(self) -> None:
        os.makedirs(self.destination_path, exist_ok=True)

        for file_name in os.listdir(self.path):
            if file_name.endswith('.json'):
                file_path = os.path.join(self.path, file_name)
                data = self.load_json(file_path)
                schema = self.process_json(data)
                schema_output_path = os.path.join(self.destination_path, file_name)
                self.write_to_file(schema, schema_output_path)
                print(f"{file_path} has been processed and written to {schema_output_path}")
