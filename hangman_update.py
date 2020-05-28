# Write your code here
import random


def show(output):
    print()
    print(output)


print("H A N G M A N\n")
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)

out = len(word) * "-"
guess_list = []
life = 0
print(out)
while True:
    guess_letter = input("Input a letter: ")
    if guess_letter in word:
        guess_list.append(guess_letter)

    if guess_letter not in word:
        print("No such letter in the word")
        print()
        life += 1
        print(out)

    if guess_list.count(guess_letter) > 1:
        life += 1
        print("No improvements")

    for i in range(0, len(word)):
        if guess_letter == word[i]:
            out = out[:i] + guess_letter + out[i + 1:]

    if out == word:
        print('You guessed the word!')
        print('You survived!')
        exit()

    if (life < 8) and (guess_letter in word):
        show(out)

    if life == 8:
        print("You are hanged!")
        break
