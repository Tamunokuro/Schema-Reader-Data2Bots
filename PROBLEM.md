# Objective
Write a genertic program that:
- Reads a JSON file similar to what's present in this location (./data/)
- Sniffs the schema of the JSON file 
- Dumps the output in (./schema/)

# Additional informations for test cases
- - Padding: All attributes in the JSON schema should be padded with "tag" and "description" keys
- The schema output must capture ONLY the attributes within the "message" key of the input JSON source data (see line 8 in the input JSON files). All attributes withn the key "attributes" should be excluded
- The JSON schema should set all properties "required": false
- For data types of the JSON schema:
STRING: program should identify what is a string and map accordingly in JSON schema output
INTEGER: program should identify what is an integer and map accordingly in JSON schema output
ENUM: When the value in an array is a string, the program should map the data type as an ENUM 
ARRAY: When the value in an array is another JSON object, the program should map the data type as an ARRAY 

# Example of expected output
./schema/example.json

# Grades
1. Does your program work and does it return the expected output (40%)
2. Did you follow software best practices and python coding standard  (25%)
3. Did you write unittests for your program (25%)

# Submission
- Create a github repo, push your project and send us the link
- Add all dependcies to enable program run successfully
- A seperate main.py should be use for executing the program seamlessly
- Provide any necessary information for running the program in README.md