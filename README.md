# Проект YaCut на Flask

## Описание

Проект YaCut — это сервис укорачивания ссылок. Его назначение — связать длинную пользовательскую ссылку с короткой, которую предлагает пользователь или предоставляет предлагаемый сервис. API сервиса доступен всем желающим.

## Применяемые технологи

[![Python](https://img.shields.io/badge/Python-3.8-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0.2-blue?style=flat-square&logo=Flask&logoColor=3776AB&labelColor=d0d0d0)](https://flask.palletsprojects.com/en/latest/)

Расширения для Flask:

[![flask-sqlalchemy](https://img.shields.io/badge/Flask_SQLAlchemy-2.5.1-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
[![Flask-wtf](https://img.shields.io/badge/Flask_WTF-1.0.0-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://flask-wtf.readthedocs.io/en/latest/)
[![Flask-Migrate](https://img.shields.io/badge/Flask_Migrate-3.1.0-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://flask-migrate.readthedocs.io/en/latest/index.html)

## Запуск сервиса

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/IrinaSMR/yacut.git
```

```
cd yacut
```

Создать файл и заполнить файл .env:

```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv

source venv/scripts/activate
```

Обновить pip и установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

Создать базу данных, последовательно выполнив следующие команды:

```
flask shell

from yacut import db; db.create_all(); exit()
```

Выполнить запус сервиса:

```
flask run
```

## Доступ к сервису

```
http://127.0.0.1:5000/
```

### Доступ к API сервиса
```
http://127.0.0.1:5000/api/id/
```

### Примеры запросов к API (например, через Postman)


#### Создание новой короткой ссылки:

**POST**-запрос:

```
http://127.0.0.1:5000/api/id/
```

Тело запроса:

```json                                              
{
  "url": "https://pydocs.ru/zadachi-na-stroki-python/#alphabetsort", 
  "custom_id": "myshorturl"
}
```

Ответ:

```json
{
    "short_link": "http://127.0.0.1:5000/myshorturl",
    "url": "https://pydocs.ru/zadachi-na-stroki-python/#alphabetsort"
}
```

#### Получение оригинальной длинной ссылки по указанному короткому идентификатору:

**GET**-запрос:

```
http://127.0.0.1:5000/api/id/myshorturl
```

Ответ:

```json
{
    "url": "https://pydocs.ru/zadachi-na-stroki-python/#alphabetsort"
}
```


## Автор:
IrinaSMR
