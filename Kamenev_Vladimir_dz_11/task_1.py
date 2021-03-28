class Date:
    def __init__(self, date_string):
        self.date_string = date_string
        Date.pars_date(self.date_string)

    @classmethod
    def pars_date(cls, string):
        pars_date = [int(i) for i in string.split("-")]
        print(pars_date)
        Date.validation_date(pars_date)
        if Date.validation_date(pars_date) == False:
            print("Введена некорректная дата")

    @staticmethod
    def validation_date(in_date):
        dic = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if in_date[2] < 1:
            return False
        elif in_date[1] < 1 or in_date[1] > 12:
            return False
        elif in_date[1] == 2:
            if in_date[2] % 4 == 0:
                if in_date[0] < 1 or in_date[0] > 29:
                    return False
            elif in_date[0] < 1 or in_date[0] > 28:
                return False
        elif in_date[0] < 1 or in_date[0] > dic[in_date[1]]:
            return False
        else:
            return True


dt = Date("29-02-2020")
dt1 = Date("29-02-2021")
