import json
profit = {}
av_profit = {}
main_list = []
sum = 0
count = 0
with open('5_7_file.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        sum += int(earning)
        count += 1
    av_profit['average'] = sum / count
    main_list.append(profit)
    main_list.append(av_profit)
print(main_list)
with open('5_7_file_j.json', 'w') as js:
    json.dump(main_list, js)

