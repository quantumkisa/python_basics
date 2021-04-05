string = input('Введите строку из нескольких слов, разделенных пробелом')
list_from_str = string.split()
num = 1
for el in range(string.count(' ') + 1):
    if len(list_from_str[el]) <= 10:
        print(f" {num} {list_from_str [el]}")
        num += 1
    else:
        print(f" {num} {list_from_str [el] [0:10]}")
        num += 1