#load files ending .json
# read the schema from the folder /data
# dump the data in the folder /schema
from json_loader import JSONReader

def main():

    # Specify the input directory containing JSON files
    input_directory = 'data'
    
    # Specify the output directory for the schema files
    output_directory = 'schema'

    processor = JSONReader(input_directory, output_directory)

    processor.process_json_files()


if __name__ == "__main__":
    main()