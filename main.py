import smtplib
import imaplib
import email
from time import sleep
import colorama
from colorama import Fore, Back, Style


email = input('Введите желаемое имя почты без домена: ')
#Список для расширения доменов
emailist = [f'{email}@yandex.ru',f'{email}@gmail.com',f'{email}@outlook.com',f'{email}@mail.ru']



colorama.init()
print(f'Почты для поиска: {emailist}')
print('Среднее время поиска всех почт - 40 секунд')
connection = imaplib.IMAP4_SSL('imap.gmail.com')
connection.login('botdeadcsgo@gmail.com','BotCSGOalax')
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('botdeadcsgo@gmail.com','BotCSGOalax')
smtpObj.set_debuglevel(0)
for email in emailist:
    status, msgs = connection.select('INBOX')
    assert status == 'OK'
    typ, data = connection.search(None, 'ALL')
    smtpObj.sendmail("botdeadcsgo@gmail.com",email,"Test")
    sleep(10)
    status, msgs = connection.select('INBOX')
    assert status == 'OK'
    typ, data1 = connection.search(None, 'ALL')
    if data1 == data:
        
        print(Fore.RED + f'Почта {email} существует')
    else:
        Fore.GREEN
        print(Fore.GREEN + f'Почта {email} не существует')

smtpObj.quit()
connection.close()
connection.logout()