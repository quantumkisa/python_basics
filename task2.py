from random import choice, random
import pandas as pd
# получаем список рандомных образцов
with open("Annotation.txt") as f:
    my_list = f.read().split('\n')
    new_list = []
    for i in range(len(my_list)):
        if i == 0: # избавлемся от первой строки с названиями
            continue
        a = my_list[i].split()
        new_list.append(a)
new_list.pop() # избавляемся от последней строки - пустого списка
new_list.sort(key=lambda el: el[1]) # сортируем по названию клеток.
list_err_srr = []
for j in range(1):
    # в этом цикле мы будем проходиться по названиям клеток и в
    # переменную current_list записывать нмоера клеток с одинаковым названием,
    # а потом из них выбирать рандомную и записывать в exit_list.
    # далее очищать current_list и заново записывать в него уже следующий тип клеток.
    comparable = new_list[0][1]
    current_list = []
    exit_list = []  # список образцов от каждого вида клеток
    list_of_cells_names = [] # ведем список всех названий клеток
    for el in new_list:
        if el[1] == comparable:
            current_list.append(el[0])
        else:
            list_of_cells_names.append(comparable)
            comparable = el[1]
            exit_list.append(choice(current_list))
            current_list.clear()
    df = pd.read_csv("cells_expressions.tsv", sep='\t')
    # получаем список чисел от 0-1 в сумме дающие 1
    r = [random() for i in range(10)]
    s = sum(r)
    r = [i / s for i in r]  # список коэффициентов, дающих в сумме 1
    print(sum(r))
    # получим результат смеси
    current_list_expr = 0
    final_list_expr = 0  # финальное значение
    coefficients = []
    dict_for_table_1 = {"клетки": list_of_cells_names, "доли клеток": coefficients}
    for i in exit_list:
        index = choice(r)
        coefficients.append(index)
        r.remove(index)
        current_list_expr = index * sum(df[i].tolist())
        final_list_expr += current_list_expr
    table_1 = pd.DataFrame(dict_for_table_1) # таблица с названиями клеток и их долями в смеси
    print(table_1)



