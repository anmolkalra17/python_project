total = 0
mean = 0
count = 0

while True:
    num = input()
    if num != '.':
        count += 1
        total += int(num)
        mean = total / count
        continue

    if num == '.':
        break
print(mean)
