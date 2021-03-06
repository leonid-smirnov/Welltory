# Welltory

#### Веб-сервис для обработки данных.

#### Контекст задачи:

    у нас есть пользователи от которых мы получаем некоторые данные мы получаем данные каждый день, таким образом каждая точка данных соответствует некоторой дате
    все данные имеют тип float
    в результате сбора данных мы имеем массивы вида [{"date": ..., "value": ...}, {"date": ..., "value": ...}, ...]
    видов (например шаги, средняя частота пульса и тп) данных может быть много, в рамках этой задачи будем считать, что они однозначно различаются по строковому    названию (см. примеры запросов к АПИ ниже)

#### ТЗ выглядит следующим образом:

    Реализовать HTTP веб-сервис. Сервис должен предоставлять HTTP API с помощью которого можно посчитать корреляцию по Пирсону между 2 векторами данных разных типов
    При расчете корреляции требуется сопоставить потоки между собой с учетом дат, то есть мы "сравниваем" два показателя за одну и ту же дату, а не как попало
    Полученные результаты должны сохраняться в базу данных.
    Данные сохраненные в БД также должны быть впоследствии доступны через API.

#### API

    POST /calculate

    Принимает входные данные в JSON-формате:

#### Настройка среды разработки

REST API DEV Django + MYSQL + DOCKER Проверка через POSTMAN Django: POST, PUT, GET, DELETE requests

#### Настройка и сборка Docker

1. Собрать и запустить докер-контейнер (по инструкции ниже)
   1.1 Собрать контейнер

> docker-compose -f docker-compose.yml build

1.2 Запустить контейнер
> docker-compose -f docker-compose.yml up

#### Остановка контейнера (можно повторно запустить):

> docker-compose -f docker-compose.yml stop

#### Остановка контейнера с удалением контейнера

> docker-compose -f docker-compose.yml down

#### Остановка контейнера с удалением контейнера и волюмов БД

> docker-compose -f docker-compose.yml down -v

#### Добавить суперпользователя (для захода в админку):

1. Смотрим список запущенных контейнеров командой:

> docker-compose ps -a

2. После первого запуска docker делаем миграции.

> docker exec -it welltory_web_1 python manage.py makemigrations
> docker exec -it welltory_web_1 python manage.py migrate

3.Находим контейнер с "web" в имени. Добавляем суперпользователя командой (web_1 - имя контейнера из п.1):
> docker exec -it web_1 python manage.py createsuperuser
