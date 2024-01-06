import string
import random

alpha_lowercase = list(string.ascii_lowercase)
alpha_uppercase = list(string.ascii_uppercase)
numbers = list(range(0, 10))
special_char = list(string.punctuation)

print("Welcome to Passowrd Creator")

total_alpha = int(input("How many letters do you like in your password\n"))
total_special = int(input("How many symbols do you like in your password\n"))
total_numbers = int(input("How many numbers do you like in your password\n"))

password_list = []

for i in range(1, total_alpha + 1):
    password_list.append(random.choice(alpha_lowercase))

for i in range(1, total_special + 1):
    password_list.append(random.choice(special_char))

for i in range(1, total_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password_final = "".join(str(element) for element in password_list)

print(f"Your Password is \n{password_final}")