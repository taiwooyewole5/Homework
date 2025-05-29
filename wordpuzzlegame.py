# Word Guessing Game (Wordle-style)
# Extra Feature: Uses a list of Bible names for the secret word!
# Extra Feature: Replay option after each round

import random

# Bible name list
word_list = ["matthew", "mark", "luke", "john", "peter", "simon", "philip"]

def play_game():
    secret_word = random.choice(word_list).lower()

    print("\nWelcome to the word guessing game!\n")
    print(f"Your hint is: {'_ ' * len(secret_word)}")

    guess_count = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = input("What is your guess? ").lower()
        guess_count += 1

        if len(guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word.")
            continue

        if guess == secret_word:
            guessed_correctly = True
            break

        # Build the hint
        hint = ""
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                hint += guess[i].upper() + " "
            elif guess[i] in secret_word:
                hint += guess[i].lower() + " "
            else:
                hint += "_ "

        print(f"Your hint is: {hint.strip()}")

    print("Congratulations! You guessed it!")
    print(f"It took you {guess_count} guess{'es' if guess_count > 1 else ''}.")

# Main game loop with replay option
keep_playing = "yes"
while keep_playing == "yes":
    play_game()
    keep_playing = input("\nWould you like to play again? (yes/no): ").lower()
    while keep_playing not in ["yes", "no"]:
        keep_playing = input("Please enter 'yes' or 'no': ").lower()

print("Thanks for playing! Goodbye.")
