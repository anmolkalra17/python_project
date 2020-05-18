# Write your code here
water = 400
milk = 540
beans = 120
cups = 9
money = 550
# remaining action
def remaining():
    print('The coffee machine has:')
    print(water, 'of water')
    print(milk, 'of milk')
    print(beans, 'of coffee beans')
    print(cups, 'of disposable cups')
    print(money, 'of money')
# buy action
def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    cmd = input()
    if cmd == 'back':
        pass
    else:
        global water
        global beans
        global money
        global milk
        global cups
        num = int(str(cmd))
        avl_list = [water, milk, beans, cups]
        ingridients = ['water', 'milk', 'coffee beans', 'disposable cups']
        if num == 1:
            req_list = [250, 0, 16, 1]
            for i in range(4):
                if avl_list[i] < req_list[i]:
                    print(f'Sorry, not enough {ingridients[i]}!')
                    break
            else:
                print('I have enough resources, making you a coffee!')
                water -= 250
                beans -= 16
                cups -= 1
                money += 4
        elif num == 2:
            req_list = [350, 75, 20, 1]
            for i in range(4):
                if avl_list[i] < req_list[i]:
                    print(f'Sorry, not enough {ingridients[i]}!')
                    break
            else:
                print('I have enough resources, making you a coffee!')
                water -= 350
                milk -= 75
                beans -= 20
                cups -= 1
                money += 7
        elif num == 3:
            req_list = [200, 100, 12, 1]
            for i in range(4):
                if avl_list[i] < req_list[i]:
                    print(f'Sorry, not enough {ingridients[i]}!')
                    break
            else:
                print('I have enough resources, making you a coffee!')
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1
                money += 6
# fill action
def fill():
    print('Write how many ml of water do you want to add:')
    add_water = int(input())
    print('Write how many ml of milk do you want to add:')
    add_milk = int(input())
    print('Write how many grams of coffee beans do you want to add:')
    add_beans = int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    add_cups = int(input())
    global water
    global beans
    global milk
    global cups
    water += add_water
    milk += add_milk
    beans += add_beans
    cups += add_cups
# take action
def take():
    global money
    print('I gave you $' + str(money))
    money = 0
# main cycle
def main_cycle():
    while True:
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()
        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'remaining':
            remaining()
        else:
            break


main_cycle()
