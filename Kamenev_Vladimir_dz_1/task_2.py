degrees = []
for i in range(1, 1000):
    if i % 2 != 0:
        degrees.append(i ** 3)
_sum1 = 0
_sum2 = 0
for i in degrees:
    _sum = 0
    _sum17 = 0
    number = i
    number17 = number + 17
    for j in range(len(str(i))):
        digit = number % 10
        number = number // 10
        _sum += digit

        digit = number17 % 10
        number17 = number17 // 10
        _sum17 += digit

    if _sum % 7 == 0:
        _sum1 += i

    if _sum17 % 7 == 0:
        _sum2 += i + 17

print("Сумма в первоначальном списке чисел, которые деляться на 7 - ", _sum1)
print("Сумма чисел в списке увеличенном на 17, которые деляться на 7 - ", _sum2)
