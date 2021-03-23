from abc import ABC, abstractmethod


class Clothes(ABC):
    rez = 0

    def __init__(self, param):
        self.V = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.rez += (self.consumption + other.consumption)
        return Coat(0)

    def __str__(self):
        if Clothes.rez == 0:
            self._rez = self.consumption
        else:
            self._rez = Clothes.rez
        Clothes.rez = 0
        return f"Для пошива выбранной вами одежды необходимо {self._rez:.2f}м ткани."


class Coat(Clothes):

    @property
    def consumption(self):
        self.cons = 0
        if self.V > 0:
            self.cons = self.V / 6.5 + 0.5
        return self.cons


class Suit(Clothes):

    @property
    def consumption(self):
        self.cons = 0
        if self.V > 0:
            self.cons = 2 * self.V / 100 + 0.3
        return self.cons


coat = Coat(55)
print(coat)

suit = Suit(180)
print(suit)

suit1 = Suit(175)
print(suit1)

print(coat + suit + suit1)
print(coat + suit)
