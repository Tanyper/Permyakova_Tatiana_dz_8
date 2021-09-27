import re

def email_parse(email_address):
    list_email =re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not list_email.match(email_adress):
        raise ValueError (f'wrong email:{email_adress}')
    print (list_email.match(email_adress).groupdict())
    for i in ['someone@geekbrains.ru','someone@geekbrainss.ru','someone@geekbrainsru']:
        try:
            email_parse(i)
        except ValueError as err:
            print (error)