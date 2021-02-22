from task_3 import currency_rates

currency_request = input('Введите интересующую вас валюту: ')

if len(currency_request) != 3:
    print('Не верно указана наменклатура валюты')
else:
    currency_cource = currency_rates(currency_request)
    if currency_cource:
        print(f'На {currency_cource[1]} курс {currency_request.upper()} равен {currency_cource[0]}руб.')
    else:
        print(currency_cource)
