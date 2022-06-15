# Python standard libraries
import os

working_directory = os.path.abspath(os.path.dirname(__file__))
input_directory = os.path.join(working_directory, 'sample-data')

print('\nStarting…\n')

# Loop through files in input directory
for root, dirs, files in os.walk(input_directory):
  
  # Print information about folders
  print('Number of folders: {0}'.format(len(dirs)))
  for directory in dirs:
    full_path = os.path.join(root, directory)
    print('  {0}'.format(full_path))
  
  # Print information about files
  print('Number of files: {0}'.format(len(files)))
  for file in files:
    full_path = os.path.join(root, file)
    file_type = file.split('.')[1]
    print('  {0}: {1}'.format(file_type, full_path))
    
print('\nDone!')
