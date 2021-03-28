class Warehouse():

    def __init__(self, address, number_place):
        self.address = address
        self.number_place = number_place
        self.free_place = {i for i in range(1, number_place + 1)}
        self.occupied_place = set()
        self.equipment_in_warehouse = {}

    def acceptens(self, equipment):
        self.dic = {key: item for key, item in equipment.__dict__.items()}
        self.dic.pop('name')
        self.dic.pop('quantity')
        self.dic.pop('place')
        if equipment.quantity <= len(self.free_place):

            if equipment.__class__.__name__ not in self.equipment_in_warehouse:
                self.equipment_in_warehouse[equipment.__class__.__name__] = {}
            if equipment.name not in self.equipment_in_warehouse[equipment.__class__.__name__]:
                self.equipment_in_warehouse[equipment.__class__.__name__][equipment.name] = {"quantity": 0,
                                                                                             "place": set()}
            self.equipment_in_warehouse[equipment.__class__.__name__][equipment.name]["quantity"] += equipment.quantity
            self.equipment_in_warehouse[equipment.__class__.__name__][equipment.name].update(self.dic)
            for i in range(0, equipment.quantity):
                self.new_plase = self.free_place.pop()
                self.occupied_place.add(self.new_plase)
                self.equipment_in_warehouse[equipment.__class__.__name__][equipment.name]["place"].add(self.new_plase)
        else:
            print(f"На складе осталось только {len(self.free_place)} свободных мест")

    def availability(self, grup, name_request, quantity_request, unit):
        self.grup = grup
        self.name_request = name_request
        self.quantity_request = quantity_request
        self.unit = unit
        try:
            if self.equipment_in_warehouse[grup][name_request]:
                if self.equipment_in_warehouse[grup][name_request]['quantity'] >= self.quantity_request:
                    print("ТМЦ есть на складе")
                    self.delivery()
                    return True
                else:
                    print(f"На складе только {self.equipment_in_warehouse[grup][name_request]['quantity']} ТМЦ")
                    return False
        except KeyError:
            print("ТМЦ отсутствует на складе")
            return False

    def delivery(self):
        self.equipment_in_warehouse[self.grup][self.name_request]['quantity'] -= self.quantity_request
        for i in range(0, self.quantity_request):
            self._place = self.equipment_in_warehouse[self.grup][self.name_request]['place'].pop()
            self.occupied_place.remove(self._place)
            self.free_place.add(self._place)
        print(f'ТМЦ по заявке {self.unit} отгружены')


class Office_Equipment():

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.place = {}


class Printer(Office_Equipment):

    def __init__(self, name, quantity, type):
        super().__init__(name, quantity)
        self.type = type


class Scaner(Office_Equipment):

    def __init__(self, name, quantity, size):
        super().__init__(name, quantity)
        self.size = size


def validation_grup(grup_number, guid):
    try:
        _grup = int(grup_number)
        if _grup > 3 or _grup < 1:
            print("Данной группы нет в справочнике. Попробуйте ввести еще раз")
            _grup = 0
        else:
            return guid[_grup]
    except:
        print("Данной группы нет в справочнике. Попробуйте ввести еще раз")
        _grup = 0
    else:
        return _grup


# _____________________Задание 4__________________________________________
# создаем склад с указанием адреса и количества мест хранения ТМЦ
wh = Warehouse("Минск, ул. Солтыса, 10", 2000)

# создаем экземпляры классов ТМЦ
printer = Printer("HP3000", 3, "laser")
printer1 = Printer("HP3005", 2, "laser")
scan = Scaner("Hitachy", 4, "A3")
scan1 = Scaner("Epson", 5, "A4")

# _____________________Задание 5__________________________________________
# заносим ТМЦ в базу учета на складе
wh.acceptens(printer)
wh.acceptens(printer1)
wh.acceptens(scan)
wh.acceptens(scan1)

# перечень ТМЦ на складе
print(wh.equipment_in_warehouse)

# проверка наличия ТМЦ на складе и отгрузка для запрашиваемого подразделения
print("Заявка 1")
if wh.availability("Printer", "HP31000", 2, "Технический отдел"):
    print("Заявка закрыта")

print("Заявка 2")
if wh.availability("Printer", "HP3000", 20, "Технический отдел"):
    print("Заявка закрыта")

print("Заявка 3")
if wh.availability("Printer", "HP3000", 2, "Технический отдел"):
    print("Заявка закрыта")

# проверка остатков на складе
print(wh.equipment_in_warehouse)

# _____________________Задание 6__________________________________________
# валидация корректности ввода группы ТМЦ

guid = {1: 'Printer', 2: 'Scaner', 3: -1}
mask = {'Printer': ["марку ТМЦ ", "количество ТМЦ ", "тип ТМЦ "],
        'Scaner': ["марку ТМЦ ", "количество ТМЦ ", "размер бумаги "]}
grup = 0
while grup != -1:
    param = []
    grup = validation_grup(input("Введите категорию ТМЦ: \n1 - принтер\n2 - сканер \n3 - выход\n"), guid)
    if grup != 0 and grup != -1:
        for i in range(0, 3):
            param.append(input(f"Введите {mask[grup][i]}"))

        exec(f'tmc = {grup}("{param[0]}", {int(param[1])}, "{param[2]}")')
        wh.acceptens(tmc)

# Вывод заполненной складской базы
print(wh.equipment_in_warehouse)
