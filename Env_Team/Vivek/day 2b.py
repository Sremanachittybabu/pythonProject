import re
import string

#  This function will take string and the color as input and find the largest number of balls drawn for that color
def find_count(line,color):

    greatest_number = 0

    # Pattern matches any line with combination " 1 color"
    pattern = re.compile(r'\b(\d+)\s' + re.escape(color) + r'\b')
    x = pattern.finditer(line)

    # If there is any match the below logic will pick the number alone( group(1)) . if any of that number is greater
    # than previous number, that number will be stored as greatest number.

    for matches in x:
        number = int(matches.group(1))
        if number > greatest_number:
            greatest_number = number

    return greatest_number

match_number = 0
match_multiply=0
match_sum = 0

#  Open file and read all lines into list
with open("day2.txt") as h:
    content = h.readlines()


for line in content:

    #  call the function for each color
    green_flag = find_count(line,"green")
    red_flag = find_count(line, "red")
    blue_flag = find_count(line, "blue")

    #  multiply the greatest number for all colors and add it to total sum
    match_multiply = red_flag * green_flag * blue_flag
    match_sum += match_multiply

print(f"match sum is {match_sum}")

