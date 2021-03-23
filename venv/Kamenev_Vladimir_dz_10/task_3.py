class Cage:
    def __init__(self, cell_qwentity):
        self.cell_qwentity = cell_qwentity

    def __add__(self, other):
        return self.cell_qwentity + other.cell_qwentity

    def __sub__(self, other):
        self.sub_cage = self.cell_qwentity - other.cell_qwentity
        if self.sub_cage <= 0:
            print('Разность ячеек клеток не может быть меньше либо равна нулю')
            self.sub_cage = "???"
        return self.sub_cage

    def __mul__(self, other):
        return self.cell_qwentity * other.cell_qwentity

    def __imul__(self, other):
        pass

    def __floordiv__(self, other):
        return self.cell_qwentity // other.cell_qwentity

    def make_order(self, cell_row):
        return "\\n".join("*" * cell_row for _ in range(self.cell_qwentity // cell_row)) + \
               "\\n" + "*" * (self.cell_qwentity % cell_row)


c = Cage(8)
c1 = Cage(3)

print(f'Сумма клеток {c + c1}')
print(f'Разность клеток {c - c1}')
print(f'Разность клеток {c1 - c}')
print(f'Умножение клеток {c * c1}')
print(f'Целая часть от деления {c // c1}')
print(c.make_order(3))
