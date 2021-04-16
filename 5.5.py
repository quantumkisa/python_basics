from random import randrange
rand_obj = [randrange(-10, 10) for i in range(randrange(5, 15))]
f_obj = open("5_5_file.txt", "w+")
f_obj.write('\n'.join(map(str, rand_obj)))
print(sum(rand_obj))
