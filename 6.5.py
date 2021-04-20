class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки маркером")


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
