import csv

# Specify the header you want to add
header = ['REG', 'RACF', 'FIRST NAME', 'LAST NAME', 'DATE','MONTH', 'YEAR']  # Replace with your actual column names

# Input and output file paths
input_file_path = 'output.csv'
output_file_path = 'output_header.csv'

# Open the original CSV file for reading
with open(input_file_path, 'r') as input_file:
    # Read the existing data
    data = list(csv.reader(input_file))

# Add the header to the data
data.insert(0, header)

# Open a new CSV file for writing with the added header
with open(output_file_path, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerows(data)

print(f'Header added to {input_file_path}. New file saved at: {output_file_path}')