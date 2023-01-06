import os
import re

def delete_duplicate_files(dir_path):
  # Get a list of all the files in the directory
  files = os.listdir(dir_path)

  # Iterate through each file
  for file in files:
    # Check if the file has a duplicate version with a number in parentheses
    match = re.search(r'(.*)\s+\((\d+)\)\.(.*)', file)
    if match:
      # Get the base name and extension of the original file
      base_name = match.group(1)
      extension = match.group(3)
      original_file = base_name + '.' + extension

      # Check if the original file exists in the directory
      if original_file in files:
        # If it does, delete the duplicate file
        os.remove(os.path.join(dir_path, file))

# Test the function
delete_duplicate_files('/path/to/directory')
