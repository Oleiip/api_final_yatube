# Проект «API для Yatube».
### Описание
API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, 
публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.
### Технологии
Python 3.7, Django 3.2, DRF, JWT + Djoser
### Запуск проекта в dev-режиме
- Клонировать репозиторий и перейти в него в командной строке.
- Установите и активируйте виртуальное окружение c учетом версии Python 3.7 (выбираем python не ниже 3.7):
```bash
py -3.7 -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
```
- Затем нужно установить все зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```
- Выполняем миграции:
```bash
python manage.py migrate
```
Создаем суперпользователя:
```bash
python manage.py createsuperuser
```
Запускаем проект:
```bash
python manage.py runserver
```
### Примеры работы с API для всех пользователей
Для неавторизованных пользователей работа с API доступна в режиме чтения,
что-либо изменить или создать не получится.
```bash
GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id
GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id
GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```
### Примеры работы с API для авторизованных пользователей
Для создания публикации используем:
```bash
POST /api/v1/posts/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Обновление публикации:
```bash
PUT /api/v1/posts/{id}/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Частичное обновление публикации:
```bash
PATCH /api/v1/posts/{id}/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Частичное обновление публикации:
```bash
DEL /api/v1/posts/{id}/
```
Получение доступа к эндпоинту /api/v1/follow/
(подписки) доступен только для авторизованных пользователей.
```bash
GET /api/v1/follow/ - подписка пользователя от имени которого сделан запрос
на пользователя переданного в теле запроса. Анонимные запросы запрещены.
```
- Авторизованные пользователи могут создавать посты,
комментировать их и подписываться на других пользователей.
- Пользователи могут изменять(удалять) контент, автором которого они являются.

### Добавить группу в проект нужно через админ панель Django:
```bash
admin/ - после авторизации, переходим в раздел Groups и создаем группы
```
Доступ авторизованным пользователем доступен по JWT-токену (Joser),
который можно получить выполнив POST запрос по адресу:
```bash
POST /api/v1/jwt/create/
```
Передав в body данные пользователя (например в postman):
```bash
{
"username": "string",
"password": "string"
}
```
Полученный токен добавляем в headers (postman), после чего буду доступны все функции проекта:
```bash
Authorization: Bearer {your_token}
```
Обновить JWT-токен:
```bash
POST /api/v1/jwt/refresh/ - обновление JWT-токена
```
Проверить JWT-токен:
```bash
POST /api/v1/jwt/verify/ - проверка JWT-токена
```
Так же в проекте API реализована пагинация (LimitOffsetPagination):
```bash
GET /api/v1/posts/?limit=5&offset=0 - пагинация на 5 постов, начиная с первого
```
