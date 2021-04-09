def my_sum():
    sum_res = 0
    count = True
    while count == True:
        a = input('введите числа через пробел или Q для остановки программы.').split()
        res = 0
        for el in range(len(a)):
            if a[el] == 'Q':
                count = False
                break
            else:
                res += int(a[el])
        sum_res += res
        print('текущая сумма =', sum_res)
    print('итоговая сумма =', sum_res)

