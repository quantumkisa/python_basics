class Warehouse:
    def __init__(self, capacity):
        self.capacity = capacity


class OfficeEquipment:
    def __init__(self, name, quantity, price):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.list_of_equipment = []
        self.current_object = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}
        self.warehouse = []

    def transfer(self):
        try:
            object_name = input(f'Введите наименование ')
            object_price = float(input(f'Введите цену за ед '))
            object_quantity = int(input(f'Введите количество '))
            current_object = {'Модель устройства': object_name, 'Цена за ед': object_price, 'Количество': object_quantity}
            self.current_object.update(current_object)
            self.warehouse.append(self.current_object)
        except:
            return f'Ошибка ввода данных. Цена за ед и кол-во должны быть числовыми, а название строкой'

        q = input('Для выхода - Q, для продолжения - Enter')
        if q == 'Q' or q == 'q':
            return f'Весь склад - {self.warehouse}'
        else:
            OfficeEquipment.transfer(self)


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)


class Copier(OfficeEquipment):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)

