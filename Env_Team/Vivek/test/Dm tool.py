import pandas as pd

# Replace 'your_input_file.txt' and 'your_output_file.txt' with your actual file names
input_file = 'test.txt'
output_file = 'output.txt'

with open(input_file, 'r') as file:
    lines = file.readlines()

# Filter lines that start with a number and remove spaces
filtered_lines = [line.strip().replace(" ", "") for line in lines if
                  line.strip().startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))]

# Combine lines with the same key
combined_lines = {}
for line in filtered_lines:
    key = line[:10]  # Assuming the key is the first 10 characters
    content = line[10:]  # Content after the key
    combined_lines.setdefault(key, []).append(content)

# Create a DataFrame with the combined lines
df = pd.DataFrame(
    {'key': list(combined_lines.keys()), 'content': [' '.join(contents) for contents in combined_lines.values()]})

# Store the result in a new file
df.to_csv(output_file, index=False, header=False)

# Read lines from the file
file_path = 'output.txt'  # Replace 'your_file.txt' with the actual path to your file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove spaces and replace commas
modified_lines = [line.replace(' ', '').replace(',', 'TCWCUSAC ') for line in lines]

# Write the modified lines back to the file
output_file_path = 'final.txt'  # Replace 'output.txt' with the desired output file path
with open(output_file_path, 'w') as output_file:
    output_file.writelines(modified_lines)
