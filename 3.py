def my_func(a, b, c):
    sum = a + b + c
    sum -= min(a, b, c)
    return sum


print(my_func(7, 2, 3))

