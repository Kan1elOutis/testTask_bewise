# task_for_Bewise

<h1 align="center"><a target="_blank" href="">Тестовое задание для Bewise</a></h1>

### Задание
1. С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.

2. Реализовать на Python3 простой веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:
В сервисе должно быть реализовано REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}  ;

После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

3. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2., его настройке и запуску. А также пример запроса к POST API сервиса.

4. Желательно, если при выполнении задания вы будете использовать docker-compose, SqlAalchemy,  пользоваться аннотацией типов.

### БД с записями
![be](https://github.com/Kan1elOutis/testTask_bewise/blob/master/be.jpg)
### POST запрос на добавление 5 новых вопросов(возвращает последний добавленный вопрос)
![bew](https://github.com/Kan1elOutis/testTask_bewise/blob/master/bew.jpg)

### Запуск проекта
#### Создаем и активируем виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```

### Запуск на локальной машине:
#### Открываем в консоли папку backend:
```bash
cd backend
```

#### Обновиляем pip и ставим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate --noinput
```

#### Создайте суперпользователя Django:
```bash
python manage.py createsuperuser
```

#### Запускаем сервер:
```bash
python manage.py runserver
```

### Для запуска в Docker:
#### Переходим в папку с файлом docker-compose.yaml:
```bash
cd docker
```

### Перед запуском сервера, необходимо создать .env
### Ниже представлены параметры по умолчанию.
```bash
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=bewise_username
POSTGRES_PASSWORD=bewise
POSTGRES_DB=bewise_db
DB_ENGINE=django.db.backends.postgresql
DJANGO_SETTINGS_MODULE=bewise.settings
```

#### Запуск docker-compose:
```bash
docker-compose up -d --build
```

#### Примените миграции:
```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate --noinput
```

#### Создайте суперпользователя Django для входа в админку:
```bash
docker-compose exec backend python manage.py createsuperuser
```

#### После успешной сборки, на сервере выполните команды (только после первого деплоя):
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

#### Останавливаем контейнеры:
```bash
docker-compose down -v
```mast

#### Теперь по адресу http://localhost:8000/admin/ доступна админка.
