import os

def extract_files_to_text(directory, output_file):
    # Open the output file in write mode
    with open(output_file, 'w') as outfile:
        # Walk through the directory tree
        for root, dirs, files in os.walk(directory):
            # Process each file in the current directory
            for filename in files:
                file_path = os.path.join(root, filename)
                
                # Write the file path as header
                outfile.write(f'File: {file_path}\n')
                outfile.write('-' * 40 + '\n')
                
                # Open and read the file content
                try:
                    with open(file_path, 'r', errors='ignore') as infile:
                        # Write the file content to the output file
                        outfile.write(infile.read())
                        outfile.write('\n\n')  # Add extra newlines for separation
                except Exception as e:
                    # Handle exceptions (e.g., permission errors or encoding issues)
                    outfile.write(f'Error reading file: {e}\n')
                    outfile.write('\n\n')  # Add extra newlines for separation

# Specify the directory and the output file
directory = 'E:/sih/innovation_startup' # Change this to your directory
output_file = 'output.txt'

# Call the function
extract_files_to_text(directory, output_file)



