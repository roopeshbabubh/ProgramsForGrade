import random

# list of six-letter words to choose from
words_list = ["yellow", "purple", "silver", "rocket", "butter", "summer", "flower", "jungle", "pencil", "ticket"]

# Select a random word from the list
secret_word = random.choice(words_list)

# Create a list to store all the guessed letters
all_guessed_letters = []

# Create a list to store the correctly guessed letters and vowels
correctly_guessed_letters = []

# Add the vowels to the list of correctly guessed letters
for vowel in secret_word:
    if vowel in "aeiou":
        correctly_guessed_letters.append(vowel)


# Define a function to display the pattern
def display_pattern():
    for letter in secret_word:
        if letter in "aeiou":
            print(letter, end=" ")
        elif letter in correctly_guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\n")


# Display the initial pattern
display_pattern()

# Give the guesser 5 chances to guess the letters
for i in range(5):

    # Prompt the user to guess a letter
    guessed_letter = input("Guess a letter: ").lower()

    # Check if the guessed letter is a vowel
    if guessed_letter in "aeiou":
        print("Vowels are already displayed, try guessing a consonant!\n")
        continue

    # Check if the guessed letter has already been guessed
    if guessed_letter in all_guessed_letters:
        print("You have already guessed that letter!.\n")
        continue

    # Add the guessed letter to the list of guessed letters
    all_guessed_letters.append(guessed_letter)

    # Check if the guessed letter is in the secret word
    if guessed_letter in secret_word:
        print("Correct!")
        correctly_guessed_letters.append(guessed_letter)
    else:
        print("Incorrect!")

    # Display the updated pattern
    display_pattern()

    # Check if the guesser has guessed the word
    if set(correctly_guessed_letters) == set(secret_word):
        print(f"""Congratulations, you Won the Round..! 
        The word is "{secret_word}" """)
        break

# Check if the guesser has guessed the word
if set(correctly_guessed_letters) != set(secret_word):
    # The guesser has run out of chances
    print(f"""Oops! You lost all your chances to guess the letters.!.
    The word is "{secret_word}"
    Never mind, Play smart..!""")
