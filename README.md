# Django проект по выгрузке данных
Этот проект представляет собой веб-приложение, разработанное с использованием фреймворка Django и базы данных PostgreSQL.

# Требования
- Python 3.8 или выше
- Django 3.2 или выше
- PostgreSQL 13 или выше

# Установка и запуск проекта
Локальная установка
Клонирование репозитория
- git clone https://github.com/dmitry19931993/specialists.git
- cd specialists

# Установка зависимостей
Создайте виртуальное окружение и установите зависимости:
- python -m venv venv
- source venv/bin/activate  # На Windows используйте venv\Scripts\activate
- pip install -r requirements.txt

# Настройка базы данных
Создайте базу данных PostgreSQL и добавьте настройки в файл settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Применение миграций
- python manage.py makemigrations
- python manage.py migrate

# Загрузка тестовых данных
- python manage.py loaddata fixtures/organization.json
- python manage.py loaddata fixtures/user.json
- python manage.py loaddata fixtures/form_1.json
- python manage.py loaddata fixtures/form_2.json
- python manage.py loaddata fixtures/form_2.json

# Запуск сервера
- python manage.py runserver
- Откройте в браузере http://localhost:8000.

логин администратора
admin

пароль администратора
test1234


Этот README.md файл обеспечивает основную информацию о проекте, включая инструкции по установке, настройке и запуску.