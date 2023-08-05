#word guessing game in python
import random

def choose_random_word():
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']
    return random.choice(words)

def display_word(word, guesses):
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()

def play_game():
    name = input("What is your name? ")
    print("Good Luck, ", name)

    word = choose_random_word()
    guesses = ''
    turns = 12

    while turns > 0:
        display_word(word, guesses)
        
        if all(char in guesses for char in word):
            print("You Win")
            print("The word is:", word)
            break

        guess = input("Guess a character: ")

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet character.")
            continue

        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", turns, "more guesses")

            if turns == 0:
                print("You Lose")
                print("The word was:", word)

if __name__ == "__main__":
    play_game()

