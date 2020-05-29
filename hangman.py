# Write your code here
import random


def play():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)

    out = len(word) * "-"
    guess_list = []
    garbage = []
    life = 1
    print(out)
    while True:
        guess_letter = input("Input a letter: ")

        if guess_letter in word:
            guess_list.append(guess_letter)
        else:
            garbage.append(guess_letter)

        if len(guess_letter) != 1 or len(guess_letter) is None:
            print("You should input a single letter")

        elif guess_letter.isupper() or guess_letter.isnumeric() or (not guess_letter.isalpha()):
            print("It is not an ASCII lowercase letter")

        elif guess_list.count(guess_letter) > 1 or garbage.count(guess_letter) > 1:
            print("You already typed this letter ")

        elif guess_letter not in word and guess_letter.isalpha() and guess_letter.islower():
            print("No such letter in the word")
            life += 1

        for i in range(0, len(word)):
            if guess_letter == word[i]:
                out = out[:i] + guess_letter + out[i + 1:]

        if out == word:
            print('You guessed the word!')
            print('You survived!')
            exit()

        if life == 9:
            print("You are hanged!")
            exit()

        print()
        print(out)


def menu():
    print("H A N G M A N\n")
    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice == "play":
        play()
    elif choice == "quit":
        exit()


menu()
