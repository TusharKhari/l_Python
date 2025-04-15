import os

# Specify the directory you want to list
directory_path = "/"   

# Get the list of files and directories in the specified directory
try:
    directory_contents = os.listdir(directory_path)
    
    print(f"Contents of directory '{directory_path}':")
    for item in directory_contents:
        print(item)
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to access the directory '{directory_path}'.")
