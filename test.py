chicken_price = 23
goat_price = 678
pig_price = 1296
cow_price = 3848
sheep_price = 6769

money = int(input())

chicken_afford = money // chicken_price
goat_afford = money // goat_price
pig_afford = money // pig_price
cow_afford = money // cow_price
sheep_afford = money // sheep_price

if money < chicken_price:
    print("None")
elif chicken_price <= money < goat_price:
    if chicken_afford == 1:
        print("1 chicken")
    if chicken_afford > 1:
        print(str(chicken_afford) + " chickens")
elif goat_price <= money < pig_price:
    if goat_afford == 1:
        print("1 goat")
    if goat_afford > 1:
        print(str(goat_afford) + " goats")
elif pig_price <= money < cow_price:
    if pig_afford == 1:
        print("1 pig")
    if pig_afford > 1:
        print(str(pig_afford) + " pigs")
elif cow_price <= money < sheep_price:
    if cow_afford == 1:
        print("1 cow")
    if cow_afford > 1:
        print(str(cow_afford) + " cows")
elif money >= sheep_price:
    print(str(sheep_afford) + " sheep")
