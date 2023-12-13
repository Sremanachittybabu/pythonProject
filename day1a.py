def extract_calibration_values_from_file(file_path):
    # List to store extracted calibration values
    calibration_values = []

    # Open the file and read lines
    with open(file_path, 'r') as file:
        for line in file:
            # Remove leading and trailing whitespaces
            line = line.strip()

            # Ensure the line is not empty
            if line:
                # Extract the first and last digits
                first_digit = int(line[0])
                last_digit = int(line[-1])

                # Combine the digits to form a two-digit number
                calibration_value = first_digit * 10 + last_digit

                # Append the calibration value to the list
                calibration_values.append(calibration_value)

    return calibration_values

# Example usage:
file_path = '/Users/chittsc/PycharmProjects/pythonProject/inputa.txt'
result = extract_calibration_values_from_file(file_path)
print(result)