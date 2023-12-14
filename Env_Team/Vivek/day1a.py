import string

# Open the file and read all the lines into a list
with open("day1.txt") as h:
    content = h.readlines()

first = ""
second = ""
number = ""
sum1 = 0


# Check for the first and last digits from each line

for line in content:
    # Check from the beginning of line for the first digit . once found break loop
    for i in line:
        if i.isdigit():
            first = i
            break
    # Check from the end of line for the first digit . once found break loop
    for i in reversed(line):
        if i.isdigit():
            second = i
            break
    # Concatenate the digits into one number
    for i in line:
        if i == '\n':
            number = first + second
            break

# compute the sum of each number
    sum1 += int(number)
print(sum1)
