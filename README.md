# API для проекта Yatube

В API YATUBE можно получить или создать запись, комментарий, группу.

## Возможности:

- Подписка на пользователей
- Просмотр, создание, удаление и модификация постов
- Просмотр и создание групп
- Просмотр, создание, удаление и модификация комментариев
- Фильтрация по полям

## Установка:

- Для работы необходим Python версии 3.9.
- В директории с скачанным проектом нужно создать и заупстить виртуальное окружение:
  
```
python3 -m venv env
source venv/bin/activate
```

- Установка зависимостей

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

- Выполнить миграции

```
python3 manage.py migrate
```

- Запуск

```
python manage.py runserver
```

## Примеры доступных запросов

пример POST-запросов:

- http://127.0.0.1:8000/api/v1/users/
- http://127.0.0.1:8000/api/v1/posts/
- http://127.0.0.1:8000/api/v1/posts/1/

## После запуска сервера вам будет доступна документация

- http://127.0.0.1:8000/redoc

Автор: Киржаков Михаил

## Stack:

![Python 3.9](https://img.shields.io/badge/Python-3.9-brightgreen.svg?style=flat&logo=python&logoColor=white)
![Django REST Framework (DRF](https://img.shields.io/badge/Django%20REST%20Framework%20(DRF)-red?style=flat)
![REST API](https://img.shields.io/badge/REST%20API-00ff9d?style=flat)
![Djoser jwt](https://img.shields.io/badge/Djoser-jwt-00a5ff?style=flat)





- Python 3.9
- Django REST Framework (DRF)
- REST API
- Djoser
