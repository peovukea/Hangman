import random
from hangman_art import stages, logo
from hangman_words import word_list

life = 6
chosen_word = random.choice(word_list)
guess = ""
guessed = []
display = []
end_of_game = False


def is_alive():
    if life > 0:
        return True


print(logo)

# Add Blanks
for letter in chosen_word:
    display.append("_")

# Test case hint!
print(f"Psst... The word is {chosen_word}")
guess = (input("Guess a letter \n")).lower()

while not end_of_game:
    # Check the Guess and affect life
    if guess in guessed:
        print("You've already tried this letter... Lets try again.")
    else:
        if guess not in chosen_word:
            life -= 1
            print(f"Your guess '{guess}' was incorrect")
        else:
            print(f"Your guess '{guess}' was correct")
            for char in range(len(chosen_word)):
                if guess == chosen_word[char]:
                    display[char] = guess
                    guessed += guess

    # Display man and correct words
    print(stages[life])
    print(f"{' '.join(display)}")

    # Check if player is still alive and continue game if needed
    if not is_alive():
        print('You lose')
        end_of_game = True
    else:
        if '_' in display:
            guess = (input("Guess a letter \n")).lower()
        else:
            print(stages[life])
            print("You win!")
            end_of_game = True
