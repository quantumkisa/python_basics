from math import factorial


def fact(n):
    a = [factorial(i) for i in range(1, n + 1)]
    yield a


n = int(input('введите число'))
for el in fact(n):
    print(el)
