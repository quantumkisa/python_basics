from functools import reduce


def my_func(el_prev, el):
    return el_prev * el


a = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(my_func, a))

