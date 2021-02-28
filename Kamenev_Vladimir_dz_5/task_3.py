def gen_tutor_klass(tutors_list, klasses_list):
    for i in range(len(tutors_list)):
        if i + 1 <= len(klasses_list):
            yield (tutors_list[i], klasses_list[i])
        else:
            yield (tutors_list[i], None)


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Вадим', 'Ольга', 'Вероника'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

gen = gen_tutor_klass(tutors, klasses)

print(type(gen), *gen)
