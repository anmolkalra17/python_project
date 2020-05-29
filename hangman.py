# Write your code here
import random

print("H A N G M A N\n")
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)

out = len(word) * "-"
guess_list = []
not_needed = []
special_char = '+-/*!@#$%^&()_-=[]{}:;"\'<>.?|\`~ '
life = 0
print(out)
while True:
    guess_letter = input("Input a letter: ")

    if guess_letter in word:
        guess_list.append(guess_letter)

    if guess_letter.isupper() or guess_letter in special_char or guess_letter.isnumeric() or guess_letter is None:
        print("It is not an ASCII lowercase letter")
        life += 1

    if len(guess_letter) != 1 or guess_letter is None:
        print("You should input a single letter")
        life += 1

    if guess_letter not in word:
        not_needed.append(guess_letter)

    if guess_letter not in word and guess_letter.islower() and guess_letter not in special_char:
        print("No such letter in the word")
        life += 1

    if guess_list.count(guess_letter) > 1 or not_needed.count(guess_letter) > 1:
        life += 1
        print("You already typed this letter")

    for i in range(0, len(word)):
        if guess_letter == word[i]:
            out = out[:i] + guess_letter + out[i + 1:]

    if out == word:
        print('You guessed the word!')
        print('You survived!')
        exit()

    if life == 8:
        print("You are hanged!")
        exit()

    print()
    print(out)
