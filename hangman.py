
import random

# Step 1: List of words
words = [
        "apple","python","computer","mango",
        "banana","grapes","orange","watermelon",
        "strawberry","kiwi","peach","cherry",
        "blueberry","raspberry","pineapple","papaya",
        "coconut","avocado","pomegranate","guava",
        "jackfruit","lychee","dragonfruit","passionfruit",
        "tangerine","clementine","nectarine","persimmon",
        "kumquat","starfruit","durian","rambutan",
        "longan","soursop","breadfruit","salak",
        "miracle fruit","jabuticaba"
    ]

# Step 2: Select a random word
word = random.choice(words)

# Step 3: Initialize variables
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

# Step 4: Hangman drawings
stages = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

# Step 5: Start the game
print("Welcome to Hangman!")
print("Guess the hidden word, one letter at a time.")
print("You have", max_attempts, "wrong guesses allowed.")

# Step 6: Main game loop
while wrong_guesses < max_attempts:

    # Display the current drawing
    print(stages[wrong_guesses])

    # Display the word with hidden letters
    for letter in word:
        if letter in guessed_letters:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")

    print()
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)

    # Check whether the player has won
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        print("The word was:", word.upper())
        break

    # Get a letter from the player
    guess = input("Guess a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
        print("Please enter one English letter.")
        continue

    # Prevent repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Step 7: Display the losing result
if wrong_guesses == max_attempts:
    print(stages[wrong_guesses])
    print("Game over! You lost.")
    print("The word was:", word.upper())
