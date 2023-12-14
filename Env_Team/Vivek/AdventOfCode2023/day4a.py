card_count = 0
total_cards = 0


# Open file and read each line and execute the steps
with open('day4.txt', 'r') as file:
    for line in file:


        card_count +=1
        final_count = 0

        # Split the line based on ':'
        lines = line.strip().split(':')[1]
        # Split the line based on '|' after that
        parts = lines.strip().split('|')

        # numbers_before will be the winning numbers as they occur before |
        numbers_before = list(int(a) for a in parts[0].split())
        # numbers_after will be the  numbers user have as they occur after |
        numbers_after = list(int(a) for a in parts[1].split())

        # find numbers common between both sets
        matching_numbers = set(numbers_before) & set(numbers_after)
        # number of matches
        matching_count = len(matching_numbers)

        # add the points for each match
        if matching_count > 0:
            final_count = 2 ** (matching_count - 1)
        else:
            final_count = 0

        total_cards += final_count
        # print(f"for card {card_count} points is {final_count}")

print(total_cards)

