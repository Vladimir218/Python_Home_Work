from requests import get
from decimal import Decimal
import datetime


def currency_rates(currency):
    currency = currency.upper()
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.text
    if content.find(currency) == -1:
        return
    else:
        poz_date = content.find('<ValCurs Date=') + len('<ValCurs Date=')
        year_cource = int(content[poz_date + 7:poz_date + 11])
        month_cource = int(content[poz_date + 4:poz_date + 6])
        day_cource = int(content[poz_date + 1:poz_date + 3])
        date = datetime.date(year_cource, month_cource, day_cource)
        start = content.find(currency) + len(currency)
        start1 = content.find("</Name><Value>", start) + len("</Name><Value>")
        finish = content.find("</Value>", start1)
        if 0 < start1 < finish:
            content = content[start1:finish]
            content = Decimal(content.replace(',', '.'))
            content = content.quantize(Decimal("01.00"))
            return content, date


if __name__ == '__main__':
    currency_request = input('Введите интересующую вас валюту: ')

    if len(currency_request) != 3:
        print('Не верно указана наменклатура валюты')
    else:
        currency_cource = currency_rates(currency_request)
        if currency_cource:
            print(f'На {currency_cource[1]} курс {currency_request.upper()} равен {currency_cource[0]}руб.')
        else:
            print(currency_cource)
