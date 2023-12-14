import re
import string

# This function will take the string, the color and the maximum count that the color can have as input and return if the game is valid.
def find_count(line,color,max_count):

    invalid = 0

    # Pattern matches any line with combination " 1 color"
    pattern = re.compile(r'\b(\d+)\s' + re.escape(color) + r'\b')
    x = pattern.finditer(line)

    # If there is any match the below logic will pick the number alone( group(1)) . if any of that number is greater
    # than maximum count, invalid flag is returned.

    for matches in x:
        number = int(matches.group(1))
        if number > max_count:
            invalid = 1

    return invalid

# These are the maximum counts for each ball
red_final = 12
green_final = 13
blue_final = 14
match_number = 0
match_sum = 0

#  Open file and read all lines into list
with open("day2.txt") as h:
    content = h.readlines()


for line in content:
    #  match_number will store the game number.
    match_number += 1
    #  call the function for each color
    red_flag = find_count(line,"red",red_final)
    green_flag = find_count(line, "green", green_final)
    blue_flag = find_count(line, "blue", blue_final)
    # if all the balls are valid for a game, add that game number to the total sum.
    if red_flag == 0 and green_flag == 0 and blue_flag == 0:
        match_sum += match_number

print(f"match sum is {match_sum}")

