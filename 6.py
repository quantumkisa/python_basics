def int_func(my_string):
    my_list = list(my_string)
    my_list[0] = my_list[0].upper()
    my_string = ''.join(my_list)
    print(my_string)


def int_func_2(my_string):
    my_list = list(my_string)
    for i in range(len(my_list)):
        if i == 0:
            my_list[i] = my_list[i].upper()
        elif my_list[i] == ' ':
            my_list[i + 1] = my_list[i + 1].upper()
        else:
            continue
    my_string = ''.join(my_list)
    print(my_string)


my_string = input('ввведите строку с маленькой буквы')
my_string_2 = input('ввведите слова через пробел')
int_func(my_string)
int_func_2(my_string_2)





