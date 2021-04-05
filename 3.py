month = int(input("Введите номер месяца"))
if month not in range(1, 13):
    month = int(input("Введите номер месяца от 1 до 12"))
month_dict = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter'
}
print(month_dict.get(month))
