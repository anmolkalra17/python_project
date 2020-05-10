def coffee_in_machine(water_in, milk_in, coffee_in, disposable_cups_in, money_in):
    def resources_in(water_in, milk_in, coffee_in, disposable_cups_in, money_in):
        water = water_in
        milk = milk_in
        coffee = coffee_in
        cups = disposable_cups_in
        money = money_in

        def print_values():
            print("The coffee_in machine has:")
            print(str(water) + " of water")
            print(str(milk) + " of milk")
            print(str(coffee) + " of coffee beans")
            print(str(cups) + " of disposable cups")
            print(str(money) + " of money")
            print()

        print_values()

    def make_espresso(water_in, milk_in, coffee_in, disposable_cups_in, money_in):
        if water_in >= 250 and coffee_in >= 16 and disposable_cups_in >= 1:
            print("I have enough resources, making you a coffee!")
            print()
            water_in -= 250
            milk_in -= 0
            coffee_in -= 16
            money_in += 4
            disposable_cups_in -= 1
        elif water_in < 250:
            print("Sorry, not enough water!")
        elif coffee_in < 16:
            print("Sorry, not enough coffee!")
        elif disposable_cups_in < 1:
            print("Sorry, not enough disposable cups!")

    def make_latte(water_in, milk_in, coffee_in, disposable_cups_in, money_in):
        if water_in >= 350 and milk_in >= 75 and coffee_in >= 20 and disposable_cups_in >= 1:
            print("I have enough resources, making you a coffee!")
            print()
            water_in -= 350
            milk_in -= 75
            coffee_in -= 20
            money_in += 7
            disposable_cups_in -= 1
        elif water_in < 350:
            print("Sorry, not enough water!")
        elif milk_in < 75:
            print("Sorry, not enough milk!")
        elif coffee_in < 20:
            print("Sorry, not enough coffee!")
        elif disposable_cups_in < 1:
            print("Sorry, not enough disposable cups!")

    def make_cappuccino(water_in, milk_in, coffee_in, disposable_cups_in, money_in):
        if water_in >= 200 and milk_in >= 100 and coffee_in >= 12 and disposable_cups_in >= 1:
            print("I have enough resources, making you a coffee_in!")
            print()
            water_in -= 200
            milk_in -= 100
            coffee_in -= 12
            money_in += 6
            disposable_cups_in -= 1

        elif water_in < 200:
            print("Sorry, not enough water!")
        elif milk_in < 100:
            print("Sorry, not enough milk!")
        elif coffee_in < 12:
            print("Sorry, not enough coffee!")
        elif disposable_cups_in < 1:
            print("Sorry, not enough disposable cups!")

    def action(action_in, water_in, milk_in, coffee_in, disposable_cups_in, money_in):
        if action_in == "buy":
            print("What do you want?\n")
            print('1 - espresso')
            print('2 - latte')
            print('3 - cappuccino')
            print('back - to main menu')
            choice = input()

            print()

            if choice == "back":
                loop()

            if int(choice) == 1:
                make_espresso(water_in, milk_in, coffee_in, disposable_cups_in, money_in)
                loop()

            if int(choice) == 2:
                make_latte(water_in, milk_in, coffee_in, disposable_cups_in, money_in)
                loop()

            if int(choice) == 3:
                make_cappuccino(water_in, milk_in, coffee_in, disposable_cups_in, money_in)
                loop()

        if action_in == "fill":
            water_add = int(input("Write how many ml of water do you want to add:\n"))
            milk_add = int(input("Write how many ml of milk do you want to add:\n"))
            coffee_add = int(input("Write how many grams of coffee beans do you want to add:\n"))
            disposable_cups_add = int(input("Write how many disposable cups of coffee_in do you want to add:\n"))

            water_in += water_add
            milk_in += milk_add
            coffee_in += coffee_add
            disposable_cups_in += disposable_cups_add
            resources_in(water_in, milk_in, coffee_in, disposable_cups_in, money_in)
            loop()

        if action_in == "take":
            print("I gave you $" + str(money_in))
            print()
            money_in -= money_in
            loop()

        if action_in == "remaining":
            resources_in(water_in, milk_in, coffee_in, disposable_cups_in, money_in)
            loop()

    def loop():
        action_in = input("Write action (buy, fill, take, remaining, exit):\n")
        while True:
            if action_in != "exit":
                action(action_in, water_in, milk_in, coffee_in, disposable_cups_in, money_in)
            elif action_in == "exit":
                return False

    loop()


coffee_in_machine(400, 540, 120, 9, 550)
