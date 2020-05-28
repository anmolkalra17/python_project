# Write your code here
import random

print("H A N G M A N\n")
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)

out = len(word) * "-"
life = 8
guess_list = []
print(out)
while life > 0:
    guess_letter = input("Input a letter:")
    if guess_letter not in word:
        print("No such letter in word \n")
        life -= 1

    for i in range(0, len(word)):
        if guess_letter == word[i]:
            print()
            out = out[:i] + guess_letter + out[i + 1:]

        if out == word:
            print('You guessed the word!')
            print('You survived!')
            life = -1
            break

    if guess_letter in word:
        guess_list.append(guess_letter)

    if guess_list.count(guess_letter) > 1:
        print("No improvements")
        life -= 1

    print(out)

if life == 0:
    print("You are hanged!")
