my_list = [
    (1, {'название': input("Введите название первого устройства"), 'цена': input("Введите цену первого устройства"),
         'количество': input("Введите кол-во купленных устройств первого типа"),
         'eд': input("Введите единицы измерения устройства")}),
    (2, {'название': input("Введите название второго устройства"), 'цена': input("Введите цену второго устройства"),
         'количество': input("Введите кол-во купленных устройств второго типа"),
         'eд': input("Введите единицы измерения устройства")}),
    (3, {'название': input("Введите название третьего устройства"), 'цена': input("Введите цену третьего устройства"),
         'количество': input("Введите кол-во купленных устройств третьего типа"),
         'eд': input("Введите единицы измерения устройства")})
]
new_dict = {}
for el_list in my_list:
    for el_tuple in el_list:
        if type(el_tuple) == int:
            continue
        else:
            for key, value in el_tuple.items():
                if key not in new_dict:
                    new_dict[key] = [value]
                else:
                    new_dict[key].append(value)
new_dict = {key: list(set(value)) for key, value in new_dict.items()}
print(new_dict)
