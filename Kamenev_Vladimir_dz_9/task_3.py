class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


w = Worker("Иван", "Иванович", "инженер", 500, 100)
print(w.name, w.surname, w.position)
print(w._income)

p = Position("Петр", "Петрович", "начальник отдела", 1000, 500)
print(p.name, p.surname, p.position)
print(p._income)
print(p.get_full_name())
print((p.get_total_income()))
