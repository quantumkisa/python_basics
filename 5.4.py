rus_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
new_list = []
with open('5_4_file.txt') as f:
    my_list = f.read().split('\n')
    for el in my_list:
        b = el.split(' ', 1)
        new_list.append(rus_dict[b[0]] + ' ' + b[1])
    print(new_list)
with open('5_4_file_new.txt', 'w') as f_new:
    f_new.writelines(new_list)




