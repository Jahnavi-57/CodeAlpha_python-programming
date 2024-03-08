import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pear"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def display_hangman(attempts):
    hangman_pics = [
        """
         _______
        |       |
        |       O
        |      /|\\
        |      / \\
        |
        """,
        """
         _______
        |       |
        |       O
        |      /|\\
        |      /
        |
        """,
        """
         _______
        |       |
        |       O
        |      /|\\
        |
        |
        """,
        """
         _______
        |       |
        |       O
        |      /|
        |
        |
        """,
        """
         _______
        |       |
        |       O
        |
        |
        |
        """,
        """
         _______
        |       |
        |
        |
        |
        |
        """
    ]
    return hangman_pics[attempts]

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")

    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        print(display_hangman(6 - attempts))

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
            if display_word(word, guessed_letters) == word:
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            print("Oops! That letter is not in the word.")
            attempts -= 1

        print("Attempts left:", attempts)

    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was:", word)

hangman()
