class Data:

    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def extract(cls, data):
        my_data = []
        for el in data.split():
            if el != '-':
                my_data.append(el)
        return int(my_data[0]), int(my_data[1]), int(my_data[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year >= 0:
                    return f'Проверка пройдена'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'