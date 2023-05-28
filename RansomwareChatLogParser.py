import os
import jmespath
import json
def list_files_in_directory(directory_path):
    files = [name for name in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, name))]
    return files

def read_file(filepath):
    with open(filepath,'r') as file:
        content = file.read()
        return content

# Get the path of the "Not Parse" folder inside the current directory
current_directory = os.getcwd()
not_parse_folder_path = os.path.join(current_directory, "Not Parse")

# Check if the "Not Parse" folder exists
if os.path.isdir(not_parse_folder_path):
    # Get the path of the "lockbit3.0" folder inside the "Not Parse" folder
    lockbit_folder_path = os.path.join(not_parse_folder_path, "RansomwareName")

    # Check if the "lockbit3.0" folder exists
    if os.path.isdir(lockbit_folder_path):
        # List all the files inside the "lockbit3.0" folder
        files_in_lockbit = list_files_in_directory(lockbit_folder_path)

        # Create a new folder to save the processed files (if it doesn't already exist)
        processed_folder_path = os.path.join(current_directory, "Processed")
        os.makedirs(processed_folder_path, exist_ok=True)

        # Process each file in the "lockbit3.0" folder
        for file in files_in_lockbit:
            file_path = os.path.join(lockbit_folder_path, file)
            content = read_file(file_path)
            #print(content)
            # Parse the content as JSON
            try:
                json_content = json.loads(content)
            except json.JSONDecodeError:
                print(f"Error parsing JSON file: {file}")
                continue
            parsed = jmespath.search("messages[?party=='RansomwareName'].content", json_content)
            print(parsed)
            # Apply JMESPath queries to the JSON content as needed
            # For example, to extract specific data using JMESPath:
            # result = jmespath.search('<JMESPath query>', content)

            # Save the processed content as a new file in the "Processed" folder
            new_file_path = os.path.join(processed_folder_path, f"{file}.txt")
            with open(new_file_path, 'w') as new_file:
                for i in parsed:
                    new_file.write(f'{i}\n')
