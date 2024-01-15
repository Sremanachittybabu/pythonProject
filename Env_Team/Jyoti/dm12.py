import pandas as pd
input_file_path = "dminput1.txt"
# Dictionary to store rows based on keys

with open(input_file_path, 'r') as file:
    lines = file.readlines()

filtered_lines = [line.strip() for line in lines]
#print(filtered_lines)

combined_lines = {}
for line in filtered_lines:
    key = line[:18]  # Assuming the key is the first 10 characters
    content = line[19:]  # Content after the key
    combined_lines.setdefault(key, []).append(content)

#print(combined_lines)

df = pd.DataFrame(
    {'key': list(combined_lines.keys()), 'content': [' '.join(contents) for contents in combined_lines.values()]})

Temp_file_path = "out_file_test.txt"
df.to_csv(Temp_file_path, index=False, header=False)

file_path = 'out_file_test.txt'  
with open(file_path, 'r') as file:
    lines = file.readlines()

modified_lines = [line.replace(',', '') for line in lines]
# Write the modified lines back to the file
output_file_path = 'dm_final_out_check.txt'  # Replace 'output.txt' with the desired output file path
with open(output_file_path, 'w') as output_file:
    output_file.writelines(modified_lines)
