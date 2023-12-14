card_number = 0
total_cards = 0

# Since each card will be there least once create list with 1 as card count
card_count = [1] * 300

# Open file and read each line and execute the steps
with open('day4.txt', 'r') as file:
    for index, line in enumerate(file):

        card_number += 1
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

        # This will store the matching numbers for that particular card.
        loop_card_count = matching_count

        idx = card_number
        # loop_times will store the number of cards of each type the user has.
        loop_times = card_count[idx - 1]

        # execute for a card till:
        # 1. one time each for a match for a particular card
        # 2. one time per card(if there are 2 counts for a card, the loop has to be done 2 times)
        while (loop_card_count != 0) and (loop_times != 0):

            # increment card count if there is a match
            card_count[idx] += 1
            # the next card count should be incremented in next run. so incrementing the counter
            idx += 1
            # decrease the match count after each run
            loop_card_count -= 1

            #  once the match count is 0, decrease the current card count by 1 and reset the match count back to
            #  initial value
            if loop_card_count == 0:
                loop_card_count = matching_count
                idx = card_number
                loop_times -= 1

# only add cards that are present in input file
total_cards = sum(card_count[:card_number])
print(total_cards)
