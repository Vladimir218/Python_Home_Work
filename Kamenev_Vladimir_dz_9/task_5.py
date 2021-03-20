class Stationary:
    def __init__(self):
        self.title = self.__class__.__name__

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки карандашем')


class Handle(Stationary):
    def draw(self):
        print('Ручная отрисовка')


st = Stationary()
st.draw()

p = Pen()
p.draw()

pc = Pencil()
pc.draw()

h = Handle()
h.draw()
