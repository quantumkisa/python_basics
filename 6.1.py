from time import sleep
class TrafficLight:
    __color = 'red'
    def running(self):
        i = 0
        while i < 3:
            if TrafficLight.__color == 'red':
                print("Пожалуйста ожидайте. Горит красный цвет")
                sleep(7.0)
                TrafficLight.__color = 'yellow'
                i += 1
            elif TrafficLight.__color == 'yellow':
                print("Скоро включится зеленый свет")
                sleep(2.0)
                TrafficLight.__color = 'green'
                i += 1
            elif TrafficLight.__color == 'green':
                print("Переход дороги разрешен")
                sleep(20.0)
                TrafficLight.__color = 'red'
                i += 1
                print("Пожалуйста ожидайте. Горит красный цвет")

TrafficLight = TrafficLight()
TrafficLight.running()
