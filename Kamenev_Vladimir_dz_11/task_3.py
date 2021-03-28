import re


class OwnError(Exception):
    def __init__(self, text):
        self.text = text


string = ""
list_didgit = []
while string != 'stop':
    try:
        string = input('Введите число ')
        if re.match(r'-?[0-9]+', string):
            list_didgit.append(float(string))
        else:
            raise OwnError("Введено не число")
    except OwnError as err:
        print(err)

print(*list_didgit)
