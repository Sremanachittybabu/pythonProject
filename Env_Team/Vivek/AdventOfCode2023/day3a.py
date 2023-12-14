import re

# The main steps followed is as below.
#   1. Select one line and find a number if any in that line.
#   2. check if there is any special character other than '.' surrounding number (consider a box around the number
#    .....  -> Previous line
#    .123.  -> current line
#    .....  -> next line
#   3. if step 2 gives any valid number, put it in the final array
#   4. add all numbers from the final array

#  The below function will check if there is any character other than '.' in the passed string
def has_non_dot_characters(input_string):
    match = 0
    if any(char != '.' for char in input_string):
        match = 1

    return match

#  This array will store the numbers which has any special character around it(except '.')
valid_numbers = []

# read file into a list
with open("day3.txt") as file:
    content = file.readlines()

# This pattern will check for a number.
pattern_number = re.compile(r'\d+')
# This pattern will check for a special character(except '.') followed by a number.
pattern_before = re.compile(r'(?<!\.)\b\d+\b')
# This pattern will check for a special character(except '.') after a number.
pattern_after = re.compile(r'\b\d+\b(?!\.)')

for index, line in enumerate(content):

    next_index = index + 1
    prev_index = index - 1

    # Get the previous and next lines for the current line that is read.
    # If the current line is first line, move '....' to the previous line
    # If the current line is last line, move '....' to the next line

    if prev_index >= 0:
        prev_line = content[index - 1]
    else:
        prev_line = "...."
    if next_index < len(content):
        next_line = content[index + 1]
    else:
        next_line = "...."

    # matches_number has the number from a line
    matches_number = pattern_number.finditer(line)

    for i in matches_number:

        # Check if the number is at the beginning or end of the line.
        beg_of_line = 0
        end_of_line = 0
        if i.start() == 0:
            beg_of_line = 1
        if i.end() == (len(line) - 1):
            end_of_line = 1

        # If it is at beginning of line the previous and next line that are passed to function will not include
        # diagonal before number. If it is at the end the line the diagonal after number is not passed.

        if beg_of_line == 1:
            prev_values = prev_line[i.start():i.end() + 1]
            next_values = next_line[i.start():i.end() + 1]
        elif end_of_line == 1:
            prev_values = prev_line[i.start() - 1:i.end()]
            next_values = next_line[i.start() - 1:i.end()]
        else:
            prev_values = prev_line[i.start() - 1:i.end() + 1]
            next_values = next_line[i.start() - 1:i.end() + 1]

        # This flag will be set to 1 when a special character except '.' is found near to number
        valid_flag = 0

        # check if there is any special character except '.' in previous line.
        prev_match = has_non_dot_characters(prev_values)
        if prev_match == 1:
            valid_numbers.append((i.group()))
            valid_flag = 1

        # check if there is any special character except '.' in next line.
        if valid_flag == 0:
            next_match = has_non_dot_characters(next_values)
            if next_match == 1:
                valid_numbers.append((i.group()))
                valid_flag = 1

        # check if there is any special character just before the number. dont do if number is at beginning of line.
        if (valid_flag == 0) and (beg_of_line == 0):
            matches_before = pattern_before.finditer(line)
            for y in matches_before:
                # Check if the number is same . sometimes there can be 1 or more numbers in a line and the
                # special character can occur before another number
                if y.group() == i.group():
                    valid_numbers.append((y.group()))
                    valid_flag = 1

        # check if there is any special character just after the number. dont do if number is at end of line.
        if (valid_flag == 0) and (end_of_line == 0):
            matches_after = pattern_after.finditer(line)
            for z in matches_after:
                # Check if the number is same . sometimes there can be 1 or more numbers in a line and the
                # special character can occur before another number
                if z.group() == i.group():
                    valid_numbers.append((z.group()))


#  Add all the valid numbers
final_numbers = [int(a) for a in valid_numbers]
result = sum(final_numbers)
print(result)