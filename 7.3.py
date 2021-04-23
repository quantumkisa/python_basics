class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return self.quantity - other.quantity
        else:
            return f'Невозможно выполнить вычитание'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
       return self.quantity // other.quantity

    def make_order(self, cells_in_row):
        row = ''
        for i in range (self.quantity // cells_in_row):
            row += fr'{"*" * cells_in_row}\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row
