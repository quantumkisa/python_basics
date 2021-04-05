list_2 = [int(x) for x in input("Введите значения через пробел").split()]
a = 0
length_list = len(list_2)
for elem_position in range(length_list):
    if elem_position == length_list - 1:
        continue
    elif elem_position == 0 or elem_position % 2 == 0:
        a = list_2.pop(elem_position + 1)
        list_2.insert(elem_position, a)
    else:
        continue
print(list_2)
