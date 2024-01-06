print("Welcome to Bill Splitter")

bill_total = float(input("What was the total bill:\n"))
user_number = int(input("How many people to split the bill:\n"))
tip_percent = int(input("What percentage tip would you like to give(10,12 or 15):"))

tip_amount = (tip_percent * bill_total) / 100
total_amount = tip_amount + bill_total
amount_per_person = round((total_amount / user_number), 2)

print(f"Each person should pay\n{amount_per_person}")
