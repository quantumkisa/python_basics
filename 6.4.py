class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_right(self):

        print(f'{self.name} повернула направо')

    def turn_left(self):
        print(f'{self.name} повернула налево')

    def show_speed(self):
        print(f"текущая скорось {self.name} равна{self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("превышена допустимая скорость в 60 км/ч.")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("превышена допустимая скорость в 40 км/ч")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def check(self):
        if self.is_police:
            return f'{self.name} is from police department'


porsche = SportCar(200, 'White', 'Porsche', False)
mini_cooper = TownCar(50, 'pink', 'Mini Cooper', False)
hyundai = WorkCar(70, 'silver', 'Hyundai', False)
cops = PoliceCar(110, 'Blue',  'Ford', True)
print(mini_cooper.name)
print(mini_cooper.color)
print(f"{cops.name} это полицейская машина? {cops.is_police}.")
print(porsche.speed)
