# 1
a = 10
b = 15
print(a, b)
c = int(input("введите число"))
print("вы ввели -", c)
d = input("как вас зовут?")
print("ваше имя -", d)
# 2
time_in_seconds = int(input("Введите время в секундах"))
hours = time_in_seconds//3600
minutes = (time_in_seconds - hours*3600)//60
seconds = time_in_seconds - hours*3600 - minutes*60
print(f"{hours}:{minutes}:{seconds}")
# 3
n = input("Введите число")
print(int(n) + int(n*2) + int(n*3))
# 4
n = int(input("Введите целое положительное число"))
max_number = n % 10
n = n // 10
while n > 0:
    if n % 10 > max_number:
        max_number = n % 10
    n = n // 10
print(max_number)

# 5
earnings = int(input("Введите выручку"))
outgoings = int(input("Введите издержки"))
if earnings > outgoings:
    print("Фирма работает с прибылью")
    profit = earnings - outgoings
    workers = int(input("Численность сотрудников"))
    print("Рентабельность -", profit/earnings)
    print("Прибыль на одного сотрудник -", profit/workers)
elif outgoings > earnings:
    print("Фирма работает с убытком")
else:
    print("Фирма работает без убытков/прибыли")
# 6
a = int(input("введите параметр a"))
b = int(input("введите параметр b"))
day_count = 1
km_count = 0
while km_count < b:
    a += 0.1*a
    km_count = a
    day_count += 1
print("номер дня -", day_count)


