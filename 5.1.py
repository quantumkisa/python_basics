f_obj = open("5_1_file.txt", "w")
while True:
    i = input("введите строку файла. для окончания записи оставьте строчку пустой")
    if i == "":
        break
    else:
        f_obj.write(i + '\n')
f_obj.close()
