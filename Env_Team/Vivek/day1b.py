import string
import re

# Open the file and read all the lines into a list
with open("day1.txt") as h:
    content = h.readlines()

# map the letters for each number`
letters_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
sum1 = 0
count = 0

# The pattern x will match for any digit or spelled digits
for line in content:
    x = re.findall(r'(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))', line,re.IGNORECASE)

    # From the beginning of string, if patter is found check if its digit or spelled digit. if digit move it directly.
    # If spelled digit, move digit from  letters_numbers dictionary.
    if (x[0].isdigit()):
        first = str(x[0])
    else:
        first = str(letters_numbers[x[0]])

    if (x[-1].isdigit()):
        last = str(x[-1])
    else:
        last = str(letters_numbers[x[-1]])

    # after this logic same as day 1
    number = first + last
    print(line)
    print(number)
    if int(number) > 0:
        count += 1
    sum1 += int(number)

print(count)
print(sum1)





