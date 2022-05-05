# Учебный проект "Запуск API_YamDB с использованием docker-compose".

## Описание

Данный проект реализует запуск API_YamDB в контейнере с использованием docker-compose.

## Технологии

Python 3.7
Django 2.2.19
Docker-compose 3.8

## Установка

Для запуска проекта после клонирования из репозитория запустите docker-compose:

```
docker-compose up
```

При первом запуске для функционирования проекта необходимо выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

Для загрузки информации в БД воспользуйтесь fixtures.json

```
docker-compose exec web python manage.py loaddata fixtures.json
```

## Автор

Иван Лепский
