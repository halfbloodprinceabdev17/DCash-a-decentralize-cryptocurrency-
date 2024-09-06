import os

def check_files(directory):
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            files.append(file)
    
    if len(files) == 0:
        print("No files found in the directory.")
        return False
    
    # Read the contents of the first file
    first_file_path = os.path.join(directory, files[0])
    with open(first_file_path, 'rb') as f:
        first_file_content = f.read()
    
    # Compare the contents of remaining files
    for file in files[1:]:
        file_path = os.path.join(directory, file)
        with open(file_path, 'rb') as f:
            file_content = f.read()
        
        if file_content != first_file_content:
            print(f"The file {file} is different.")
            return False
    
    return True

def check():
# Specify the directory path
    directory_path = 'NodeData'
# Call the function to check the files
    return  check_files(directory_path)
        
