import csv

with open("output_header.csv", 'r') as file1:
    reader1 = csv.DictReader(file1)
    original_fieldnames = reader1.fieldnames
    data_file1 = list(reader1)

with open("racf_list.csv", 'r') as file2:
    reader2 = csv.DictReader(file2)
    data_file2 = list(reader2)

print(data_file1)
print(data_file2)

matching_records = [record for record in data_file1 if any(record['RACF'] == r['RACF'] for r in data_file2)]

print(matching_records)

# Write matching records to the output CSV file
fieldnames = reader1.fieldnames  # Assuming the field names are the same for both files
with open('compare_list.csv', 'w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(matching_records)



    # Define a mapping of original column names to new column names
    column_mapping = {
        'OriginalColumnName1': 'NewColumnName1',
        'OriginalColumnName2': 'NewColumnName2',
        # Add more mappings as needed
    }

    # Create a list of dictionaries with the new column names
    new_data = [{column_mapping.get(key, key): value for key, value in row.items()} for row in reader]

# Open a new CSV file for writing
with open(new_file_path, 'w', newline='') as new_file:
    # Define the new fieldnames based on the mapping
    new_fieldnames = [column_mapping.get(name, name) for name in original_fieldnames]

    # Create a csv.DictWriter object
    writer = csv.DictWriter(new_file, fieldnames=new_fieldnames)

    # Write the header
    writer.writeheader()

    # Write the rows with the new column names
    writer.writerows(new_data)

print(f'Data from {original_file_path} written to {new_file_path} with new column names')

