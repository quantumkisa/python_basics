def division_func(x, y):
    return x/y


a = int(input("введите делимое"))
b = int(input('введите делитель'))
if b == 0:
    b = int(input('введите второе число не равное нулю'))
div = division_func(a, b)
print(div)
