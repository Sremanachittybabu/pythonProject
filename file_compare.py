import csv

def compare_and_write_csv(file1_path, file2_path, output_path):
    # Read the content of the first CSV file into a list of dictionaries
    with open(file1_path, 'r') as file1:
        reader1 = csv.DictReader(file1)
        data_file1 = list(reader1)

    # Read the content of the second CSV file into a list of dictionaries
    with open(file2_path, 'r') as file2:
        reader2 = csv.DictReader(file2)
        data_file2 = list(reader2)

    # Find matching records based on a specific field (e.g., 'id' field)
    matching_records = [record for record in data_file1 if any(record['id'] == r['id'] for r in data_file2)]

    # Write matching records to the output CSV file
    fieldnames = reader1.fieldnames  # Assuming the field names are the same for both files
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(matching_records)

if __name__ == "__main__":
    file1_path = "file1.csv"
    file2_path = "file2.csv"
    output_path = "matching_records.csv"

    compare_and_write_csv(file1_path, file2_path, output_path)
