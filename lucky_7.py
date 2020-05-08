n = int(input())
list1 = []
for i in range(n):
    number = int(input())
    list1.append(number)
for n in list1:
    if n % 7 == 0:
        print(n ** 2)
