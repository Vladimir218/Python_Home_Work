class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.class_name = self.__class__.__name__
        print(f"Отрабатывает класс {self.class_name}")
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return (f'Машина начала движение')

    def stop(self):
        print(f'Машина остановилась')

    def turn(self, direction):
        if direction == "left":
            print(f"Машина поворачивает налево")
        elif direction == "right":
            print(f"Машина поворачивает направо")
        else:
            print(f"Машина движется без изменения направления")

    def show_speed(self):
        print(f"Машина движется со скоростью {self.speed} км/ч")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Машина движется с превышением скорости. Скорость - {self.speed}км/ч.')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Машина движется с превышением скорости. Скорость - {self.speed}км/ч.')
        else:
            super().show_speed()


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


car = Car(61, "black", "opel")
print(car.speed)
print(car.color)
print(car.name)
print(car.is_police)
car.go()
car.show_speed()
car.turn('left')
car.turn('right')
car.turn('stop')
car.stop()

tc = TownCar(61, "black", "opel")
print(tc.speed)
print(tc.color)
print(tc.name)
print(tc.is_police)
tc.go()
tc.show_speed()
tc.turn('left')
tc.turn('right')
tc.turn('stop')
tc.stop()

tc1 = TownCar(59, "red", "bmw")
tc1.show_speed()

sc = SportCar(150, "yellow", "ferary")
print(sc.speed)
print(sc.color)
print(sc.name)
print(sc.is_police)
sc.go()
sc.show_speed()
sc.turn('left')
sc.turn('right')
sc.turn('stop')
sc.stop()

wc = WorkCar(61, "black", "opel")
print(wc.speed)
print(wc.color)
print(wc.name)
print(wc.is_police)
wc.go()
wc.show_speed()
wc.turn('left')
wc.turn('right')
wc.turn('stop')
wc.stop()

wc1 = WorkCar(39, "black", "opel")
wc1.show_speed()

pc = PoliceCar(61, "black", "opel")
print(pc.speed)
print(pc.color)
print(pc.name)
print(pc.is_police)
pc.go()
pc.show_speed()
pc.turn('left')
pc.turn('right')
pc.turn('stop')
pc.stop()
