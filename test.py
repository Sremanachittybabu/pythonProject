def my_points(card):
# Extract winning numbers and your numbers
            winning_numbers_str, your_numbers_str = split_parts[1].split(" | ")
# Convert the strings to lists of integers
#            winning_numbers = list(map(int, winning_numbers_str.split()))
#           your_numbers = list(map(int, your_numbers_str.split()))
            winning_numbers = set(map(int, winning_numbers_str.split()))
            your_numbers = set(map(int, your_numbers_str.split()))
            print("Winning Numbers:", winning_numbers)
            print("Your Numbers:", your_numbers)
            common_numbers = your_numbers.intersection(winning_numbers)
            print('common_numbers:', common_numbers)
            points = 0
#            points = sum(2**(index - 1) for index, number in enumerate(sorted(common_numbers, reverse=True), start=1))
            for index, number in enumerate(sorted(common_numbers, reverse=True), start=1):
                points = 2**(index - 1)
                print('points:', points)
            return points
total_points = 0
with open('input_day4a.txt', 'r') as file:
        # Read each line from the file
        for line in file:
            split_parts = line.split(": ")
            print(split_parts)
#            total_points = sum(my_points(card) for card in split_parts)
#            Final += total_points
            points = my_points(split_parts)
            print(points)
            total_points += points
            print('tot:', total_points)