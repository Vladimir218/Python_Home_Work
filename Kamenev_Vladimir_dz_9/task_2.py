class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.calculate()

    def calculate(self):
        self.res = self._length * self._width * 25 * 5 / 1000
        return f'{self._length} м*25кг*5см = {self.res:.0f}т.'


a = Road(20, 5000)
print(a.calculate())
