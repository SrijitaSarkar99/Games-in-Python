import random
from wordlist import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses one word from the list
    while "-" in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    #letters in the chosen word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    #letters user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("\nLives remaining: ", lives)
        print("Letters you have already used: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current Word: ", " ".join(word_list)) 

        #getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("\nMessage: This letter is not in the word. You lose 1 live.")
        
        elif user_letter in used_letters:
            print("\nMessage: You have already guessed that letter. Try again..")

        else:
            print("\nMessage: Error. Invalid character. Try again..")

    if lives == 0:
        print("\nSorry, you died. The word is ", word)
    else:
        print("\nYay! You guessed the word ", " ".join(word), " correctly!")

hangman()

