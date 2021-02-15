measurement_temperature = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
digit_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
sign = ["-", "+"]
new_measurement_temperature = []
k = 0
for i in measurement_temperature:
    if digit_list.count(i[-1]) > 0:
        if sign.count(i[0]) > 0:
            if len(i) > 2:
                new_measurement_temperature.append('"')
                new_measurement_temperature.append(i)
                new_measurement_temperature.append('"')
            else:
                new_measurement_temperature.append('"')
                new_i = i[0] + "0" + i[1:]
                new_measurement_temperature.append(new_i)
                new_measurement_temperature.append('"')
        else:
            if len(i) > 1:
                new_measurement_temperature.append('"')
                new_measurement_temperature.append(i)
                new_measurement_temperature.append('"')
            else:
                new_measurement_temperature.append('"')
                new_i = "0" + i
                new_measurement_temperature.append(new_i)
                new_measurement_temperature.append('"')
    else:
        new_measurement_temperature.append(i)
count_sign = 0  # счетчик открывающих и закрывающих кавычек
message = ""
for i in new_measurement_temperature:
    if i == '"':
        if count_sign == 0:
            message += " " + i
            count_sign = 1
        else:
            message += i
            count_sign = 0
    else:
        if count_sign == 1:
            message += i
        else:
            message += " " + i
print(message)
