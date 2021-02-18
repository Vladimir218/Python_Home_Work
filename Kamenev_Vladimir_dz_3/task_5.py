import random


def gen_sequence(_list, _quantity, _repit):
    """
    функция формирования списка заданной длины, состоящий из случайной выборки элементов исходного списка
    :param _list: исходный список
    :param _quantity: количество элементов в сгенерированном списке
    :param _repit: флаг разрешения повторения элементов в сгенерированном списке
    :return: list
    """
    if _repit:
        _new_list = random.choices(_list, k=_quantity)
        return (_new_list)
    else:
        random.shuffle(_list)
        return _list[:_quantity]


def get_jokes(quantity, repit=True):
    """
    функция генерирует список, состоящий из шуток
    :param quantity: количество шуток в списке
    :param repit: флаг наличия повторений слов в шутках
    :return: list
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if not repit:
        if len(nouns) < quantity:
            quantity = len(nouns)
            print(f'Может быть сгенерировано не более {quantity} шуток')
    nouns = gen_sequence(nouns, quantity, repit)
    adverbs = gen_sequence(adverbs, quantity, repit)
    adjectives = gen_sequence(adjectives, quantity, repit)
    jokes = []
    for _word1, _word2, _word3 in zip(nouns, adverbs, adjectives):
        _word1 += " " + _word2 + " " + _word3
        jokes.append(_word1)
    return jokes


print(get_jokes(repit=False, quantity=8))
