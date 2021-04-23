class Clothes:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def am_fabric_coat(self):
        return self.width / 6.5 + 0.5

    def am_fabric_suit(self):
        return self.height * 2 + 0.3

    @property
    def am_fabric(self):
        return str(f'Общая площадь ткани на пошив одежды\n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.coat = self.width / 6.5 + 0.5

    def __str__(self):
        return f' Площадь на пальто {round(self.coat)}'


class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.suit = self.height * 2 + 0.3

    def __str__(self):
        return f' Площадь на костюм {round(self.suit)}'


coat = Coat(2, 4)

print(coat)

print(coat.am_fabric)

