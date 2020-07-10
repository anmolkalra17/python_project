# Game v1.0
import random

game_options = ['rock', 'paper', 'scissors']
game_misc = ['!rating', '!exit']
game = game_misc + game_options
score = 0

computer_choice = random.choice(game_options)

name = input()
print(f"Hello, {name}")

def rating(n):
    global score

    file = open('rating.txt', 'r')
    for line in file.readlines():
        if n in line:
            score = int(line.split()[1])
    file.close()

def game_play():
    global score
    global computer_choice

    computer_choice = random.choice(game_options)

    if user_input == "paper":
        if computer_choice == 'scissors':
            print("Sorry, but computer chose scissors")
        elif computer_choice == 'rock':
            print("Well done. Computer chose rock and failed")
            score += 100
        elif computer_choice == 'paper':
            print("There is a draw (paper)")
            score += 50

    elif user_input == "rock":
        if computer_choice == 'paper':
            print("Sorry, but computer chose paper")
        elif computer_choice == 'scissors':
            print("Well done. Computer chose scissors and failed")
            score += 100
        elif computer_choice == 'rock':
            print("There is a draw (rock)")
            score += 50

    elif user_input == 'scissors':
        if computer_choice == 'rock':
            print("Sorry, but computer chose rock")
        elif computer_choice == 'paper':
            print("Well done. Computer chose paper and failed")
            score += 100
        elif computer_choice == 'scissors':
            print("There is a draw (scissors)")
            score += 50


rating(name)
if __name__ == '__main__':
    user_input = input()

    while True:
        if user_input in game_options:
            game_play()
        elif user_input == "!rating":
            print(f"Your rating: {score}")
        elif user_input not in game:
            print("Invalid input")
        elif user_input == "!exit":
            print("Bye!")
            exit()
        user_input = input()
