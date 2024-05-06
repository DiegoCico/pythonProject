import random
import sys
from termcolor import colored


def print_menu():
    print("Lets Play wordle:")
    print("Type a 5 letter word adn hit enter! \n")


def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)


print_menu()
word = read_random_word()
print(word)

for attempt in range(1, 7):
    guess = input().lower()

    sys.stdout.write("\x1b[1A")
    sys.stdout.write("\x1b[2K")

    for i in range(min(len(guess), 5)):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end="")
        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end="")
        else:
            print(colored(guess[i], 'red'), end="")
        print()

    if guess == word:
        print(colored(f" Congratulations! You guessed the word correctly! in {attempt}", 'green'))
