numbers = []
while True:
    number = int(input())
    if number < 10:
        continue
    elif 10 < number < 100:
        numbers.append(number)
    elif number > 100:
        break

for j in numbers:
    print(j)
