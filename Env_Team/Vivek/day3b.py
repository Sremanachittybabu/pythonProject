import re

# The main steps followed is as below.
#   1. Select one line and find a '*' if any in that line.
#   2. check if there is any number surrounding * (number should have start or end near the '*'
#    ...  -> Previous line
#    .*.  -> current line
#    ...  -> next line
#   3. if step 2 gives any valid number, put it in the array .
#   4. If 2 numbers are got. multiply them.
#   5. Add all the numbers got from step 4.

#  The below function will check if there is any number in the passed string which starts or ends at start middle or end
#  position.
def has_non_dot_characters(input_string, start_pos, middle_pos, end_pos, ):

    match_num = []
    pattern_number = re.compile(r'\d+')
    matches_func = pattern_number.finditer(input_string)
    for a in matches_func:
        # a.start() will have the starting position of the number
        # a.end() will have the position after the number
        if (a.start() == start_pos) or (a.start() == middle_pos) or (a.start() == end_position) or \
                ((a.end()-1) == start_pos) or ((a.end()-1) == middle_pos) or ((a.end()-1) == end_position):
            match_num.append(a.group())

    return match_num

final_number = 0

# open the file and store in list
with open("day3.txt") as file:
    content = file.readlines()

# This pattern will check for a '*''.
pattern_ast = re.compile(r'\*')
# This pattern will check for a '*' before number'.
pattern_before = re.compile(r'\*\d+')
# This pattern will check for a '*' after number'.
pattern_after = re.compile(r'\d+\*')

for index, line in enumerate(content):

    # Get the previous and next lines for the current line that is read.
    # If the current line is first line, move '....' to the previous line
    # If the current line is last line, move '....' to the next line

    next_index = index + 1
    prev_index = index - 1

    if prev_index >= 0:
        prev_line = content[index - 1]
    else:
        prev_line = "...."
    if next_index < len(content):
        next_line = content[index + 1]
    else:
        next_line = "...."

    # matches_number has the '*' from a line
    matches_number = pattern_ast.finditer(line)

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
            start_position = i.start()
            middle_position = i.start()
            end_position = i.end()
        elif end_of_line == 1:
            start_position = i.start() - 1
            middle_position = i.start()
            end_position = i.start()
        else:
            start_position = i.start() - 1
            middle_position = i.start()
            end_position = i.end()

        # This flag will be incremented by 1 when a number is found near '*'.
        valid_flag = 0
        #  this list will store all the numbers near '*'
        num_list = []
        #  this list will store all the numbers near '*' got from previous line
        prev_match = []
        #  this list will store all the numbers near '*' got from next line
        next_match = []

        # call function to check how many number are near to '*' in previous line
        prev_match = has_non_dot_characters(prev_line, start_position, middle_position, end_position)
        if len(prev_match) > 0:
            for b in prev_match:
                num_list.append(b)
                valid_flag += 1

        # call function to check how many number are near to '*' in next line. only if 2 numbers are not got.
        if valid_flag < 2:
            next_match = has_non_dot_characters(next_line, start_position, middle_position, end_position)
            if len(next_match) > 0:
                for b in next_match:
                    num_list.append(b)
                    valid_flag += 1

        # check if there are any numbers after '*' . only if 2 numbers are not got.
        if (valid_flag < 2) and (beg_of_line == 0):
            matches_before = pattern_before.finditer(line)
            for y in matches_before:
                # Check if the number is same . sometimes there can be 1 or more '*' in a line and the
                # number can occur with any '*'.
                if y.start() == i.start():
                    # remove the '*' before appending to final list
                    num_before = ((y.group()).replace("*", ""))
                    num_list.append(int(num_before))
                    valid_flag += 1

        # check if there are any numbers before '*' . only if 2 numbers are not got.
        if (valid_flag < 2) and (end_of_line == 0):
            matches_after = pattern_after.finditer(line)
            for z in matches_after:
                # Check if the number is same . sometimes there can be 1 or more '*' in a line and the
                # number can occur with any '*'.
                if z.end() == i.end():
                    # remove the '*' before appending to final list
                    num_after = ((z.group()).replace("*", ""))
                    num_list.append(int(num_after))
                    valid_flag += 1

        # if 2 valid numbers are got near to an '*', multiply and add that result to final sum
        if len(num_list) == 2:
            num_needed = (int(num_list[0])) * (int(num_list[1]))
            final_number += num_needed
            print(num_list)


print(final_number)
