import random
import string

hangman_pics = ['''
 +---+
 |
 |
 |
 ===''', '''
 +---+
 O   |
     |
     |
 ===''', '''
 +---+
 O   |
 |   |
     |
 ===''', '''
 +---+
 O   |
/|   |
     |
 ===''', '''
 +---+
 O   |
/|\  |
     |
 ===''', '''
 +---+
 O   |
/|\  |
/    |
 ===''', '''
 +---+
 O   |
/|\  |
/ \  |
===''']

words_list = ["football", "hockey", "cricket", "rugby"]
chosen_word = random.choice(words_list)

# print(f"the chosen word is: {chosen_word}")
print("You have a total of 7 lives")

display = ["-"] * len(chosen_word)

end_of_game = "false"
lives = 7

while (end_of_game == "false") and (lives != 0):

    guess = input("Guess a letter: ").lower()

    count_word = 0
    count_lives = 0
    for x in chosen_word:
        if x == guess:
            display[count_word] = guess
            count_lives = 1
        count_word += 1

    if count_lives == 0:
        lives -= 1

    if "-" not in display:
        print("you Win")
        end_of_game = "true"
        print(f"the chosen word is: {chosen_word}")
    else:
        if lives == 0:
            print(hangman_pics[6])
            print("you Loose")
            print(f"the chosen word is: {chosen_word}")
        else:
            print(display)
            print(hangman_pics[7 - lives])
            print(f"You have {lives} lives left")
