def num_translate(translation_number):
    dictinary = {"zero": "ноль", "one": "один", "two": "два", "three": "три",
                 "four": "четыре", "five": "пять", "six": "шесть",
                 "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    if translation_number[0].islower():
        return dictinary.get(translation_number)
    else:
        return dictinary.get(translation_number.lower()).title()


english_num = input('Введите число на английском от 0 до 10 для перевода на русский язык:')
print(num_translate(english_num))
