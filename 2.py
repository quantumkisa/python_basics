def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


name = input('введите имя')
surname = input('введите фамилию')
year = (input('введите год рождения'))
city = input('введите город')
email = input('введите email')
telephone = input('введите номер телефона')
print(my_func(name, surname, year, city, email, telephone))