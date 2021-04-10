from itertools import count, cycle
for el in count(3):
    if el == 10:
        break
    else:
        print(el)
count = 0
for el in cycle('kek'):
    if count > 10:
        break
    print(el)
    count += 1
