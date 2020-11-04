class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction='лево'):
        print(f'Машина {self.name} повернула на {direction}')

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превышаете скорость!!!')
        print(f'Машина {self.name} едет со скоростью {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превышаете скорость!!!')
        print(f'Машина {self.name} едет со скоростью {self.speed}')


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


police_car = PoliceCar(100, 'black', 'RangeRower', True)
police_car.stop()
police_car.go()
police_car.show_speed()
police_car.turn()
town_car = TownCar(80, 'white', 'Audi', False)
town_car.show_speed()
print(town_car.color)
