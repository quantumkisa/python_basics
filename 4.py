def my_func(x, y):
    return x**y


def my_func_2(x, y):
    result = x
    count = abs(y)
    while count != 1:
        result *= x
        count -= 1
    result = 1 / result
    return result


x = float(input("введите действительное положительное число"))
y = int(input("введите целое отрицательное число"))
print(my_func(x, y))
print(my_func_2(x, y))