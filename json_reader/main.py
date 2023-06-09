from json_loader import JSONReader

def main():

    input_directory = 'data'
    
    output_directory = 'schema'

    schema_reader = JSONReader(input_directory, output_directory)

    schema_reader.process_json_files()

if __name__ == "__main__":
    main()