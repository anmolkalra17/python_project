# Write your code here
# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")

water_in = 400
milk_in = 540
coffee_in = 120
disposable_cups_in = 9
money_in = 550


def espresso_cost(water_in, milk_in, coffee_in, money_in):
    water_in -= 250
    milk_in -= 0
    coffee_in -= 16
    money_in -= 4


def latte_cost(water_in, milk_in, coffee_in, money_in):
    water_in -= 350
    milk_in -= 75
    coffee_in -= 20
    money_in -= 7


def cappuccino_cost(water_in, milk_in, coffee_in, money_in):
    water_in -= 200
    milk_in -= 100
    coffee_in -= 12
    money_in -= 6


def calc_cups(water_in, milk_in, coffee_in):
    n_cups = 0
    while water_in >= water_in and milk_in >= milk_in and coffee_in >= coffee_in:
        water_in -= water_in
        milk_in -= milk_in
        coffee_in -= coffee_in
        n_cups += 1
    return n_cups


# n = calc_cups(water_in, milk_in, coffee_in)
#
# needed = int(input("Write how many cups of coffee you will need:"))
# left = needed - n


def output(needed, left, n):
    if needed < n:
        print("Yes, I can make that amount of coffee (and even " + str(left) + " more than that)")
    elif needed > n:
        print("No, I can make only " + str(n) + " cups of coffee")
    elif needed == n:
        print("Yes, I can make that amount of coffee")


def resources_needed(water_in, milk_in, coffee_in, needed):
    print("For" + str(needed) + " cups of coffee you will need:")
    print(str(water_in * needed) + " ml of water")
    print(str(milk_in * needed) + " ml of milk")
    print(str(coffee_in * needed) + " g of coffee beans")


def resources_in(water_in, milk_in, coffee_in, disposable_cups_in, money_in):
    print("The coffee machine has:")
    print(str(water_in) + " of water")
    print(str(milk_in) + " of milk")
    print(str(coffee_in) + " of coffee beans")
    print(str(disposable_cups_in) + " of disposable cups")
    print(str(money_in) + " of money")

def action(action_in, water_in, milk_in, coffee_in, disposable_cups_in, money_in):
    if action_in == "buy":
        print("What do you want?\n")
        print('1 - espresso')
        print('2 - latte')
        print('3 - cappuccino')
        choice = int(input())
        print()

        if choice == 1:
            espresso_cost(water_in, milk_in, coffee_in, money_in)
            resources_in(water_in, milk_in, coffee_in, disposable_cups_in, money_in)

        if choice == 2:
            latte_cost(water_in, milk_in, coffee_in, money_in)
            resources_in(water_in, milk_in, coffee_in, disposable_cups_in, money_in)

        if choice == 3:
            cappuccino_cost(water_in, milk_in, coffee_in, money_in)
            resources_in(water_in, milk_in, coffee_in, disposable_cups_in, money_in)

    if action_in == "fill":
        water = int(input("Write how many ml of water do you want to add:\n"))
        milk = int(input("Write how many ml of milk do you want to add:\n"))
        coffee = int(input("Write how many grams of coffee beans do you want to add:\n"))
        disposable_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

        water_in += water
        milk_in += milk
        coffee_in += coffee
        disposable_cups_in += disposable_cups
        resources_in(water_in, milk_in, coffee_in, disposable_cups_in, money_in)

    if action_in == "take":
        print("I gave you $" + str(money_in))
        print()
        money_in -= money_in
        resources_in(water_in, milk_in, coffee_in, disposable_cups_in, money_in)


resources_in(water_in, milk_in, coffee_in, disposable_cups_in, money_in)

action_in = input("Write action (buy, fill, take) \n")

action(action_in, water_in, milk_in, coffee_in, disposable_cups_in, money_in)
