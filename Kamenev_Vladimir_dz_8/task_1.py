import re


def email_parse(adress):
    mail = {}
    try:
        mail = {'username': "", 'domain': ""}
        adress_patern = re.compile(r'^(([A-Za-z0-9_-]+\.)*[A-Za-z0-9_-]+)@([a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6})$')
        temp = adress_patern.findall(adress)
        if len(temp) == 0:
            raise ValueError(f'wrong email: {adress}')
        else:
            mail['username'] = temp[0][0]
            mail['domain'] = temp[0][2]
    except ValueError as err:
        print(err)
    finally:
        return mail


print(email_parse(input("Введите e-mail:")))
