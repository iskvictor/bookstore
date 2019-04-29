#Импорт необходимых модулей
import csv,sys,os

#Указываем путь до папки проекта Django в котором находится файл settings.py
project_dir = "/home/victor/django_projects/bookstore/bookstore/bookstore"

#Добавляем в переменную sys.path путь до проекта Django
sys.path.append(project_dir)

#Определяем переменную с настройками Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#Импортируем модуль Django
import django

#Загружаем настройки Django
django.setup()

#Импортируем модель Book
from book.models import Book

#Считываем CSV-файл
data = csv.reader(open("/home/victor/django_projects/bookstore/bookstore/data-bookstore.csv"),delimiter=',')

for row in data:
#Пропускаем заголовки
    if row[0] != 'name':
        product = Book()
        product.name = row[0]
        product.price= row[1]
        product.description = row[2]
        product.save()