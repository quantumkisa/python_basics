def salary(x, y, z):
    return (x * y) + z


time_hours = int(input('введите часы работы'))
wage_rate = int(input('Введите ставку/час'))
prem = int(input('введите объем премии'))
print(salary(time_hours, wage_rate, prem))
