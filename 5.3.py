with open('5_3_file.txt') as f:
    my_list = f.read().split('\n')
    sal = []
    poor = []
    for i in my_list:
        a = i.split()
        if int(a[1]) < 20000:
            poor.append(a[0])
        sal.append(int(a[1]))
    print(f"бедные {poor}, средняя зп {sum(sal) / len(sal)}")
