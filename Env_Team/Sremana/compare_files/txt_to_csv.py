import csv

# Input and output file paths
input_file_path = 'textfile.txt'
output_file_path = 'output.csv'

# Open the non-comma-separated text file for reading
with open(input_file_path, 'r') as input_file:
    # Read lines from the input file
    lines = input_file.readlines()

    # Identify the delimiter - which is space
    delimiter = ' '

    # Process the data and create a list of lists
    data = [line.strip().split(delimiter) for line in lines]

# Open the CSV file for writing
with open(output_file_path, 'w', newline='') as output_file:
    # Create a CSV writer
    csv_writer = csv.writer(output_file)

    # Write the processed data to the CSV file
    csv_writer.writerows(data)

print(f'Conversion complete. CSV file saved at: {output_file_path}')