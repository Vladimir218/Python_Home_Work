class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        sign = "+"
        if self.y + other.y < 0:
            sign = "-"
        return f'{self.x + other.x} {sign} {abs(self.y + other.y)}i'

    def __mul__(self, other):
        sign = "+"
        if self.x * other.y + other.x * self.y < 0:
            sign = "-"
        return f'{self.x * other.x - self.y * other.y} {sign} {abs(self.x * other.y + other.x * self.y)}i'


a = Complex(10, -20)
b = Complex(1, 4)

print("сложение комплексных чисел ", a + b)
print("умножене комплексных чисел ", a * b)
