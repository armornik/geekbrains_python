"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import sha256
import os.path

list_hash_site = []


def site_hash(url):
    site = url.encode()
    salt = url.split('/')[1].encode()
    res = sha256(site + salt).hexdigest()
    if not os.path.isfile('task_4.txt'):
        with open('task_4.txt', 'w'):
            ...
    if res in open('task_4.txt').read():
        print(f'Такая страница {url} уже есть')
    else:
        with open('task_4.txt', 'a') as file:
            file.write(res + '\n')


site_hash('https://www.google.com/')
site_hash('https://geekbrains.ru/')
site_hash('https://www.google.com/')
