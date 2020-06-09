# test_book_market
Тестовое задание

## Старт программы
- Необходима версия python3.6 и выше
- Установка пакетов
- `pip install -r requirements.txt`
- Выполните
- `python manage.py migrate` / `python manage.py migrate --run-syncdb`
-  Вручную создать суперпользователя, выполнив команду
- `python manage.py createsuperuser`
-  Запустить систему
- `python manage.py runserver`

## Что сделано
-  Вход/Выход из системы
-  Регистрация пользователя в системе
-  Формирование новой заявки пользователем и отправка об этом событии сообщения на почту администраторам системы
-  Получение списка книг
-  Получение списка авторов с выводом названий и количества книг автора.

## API запросы
- Для выполнения запросов необходимо зарегистрироваться и авторизоваться в системе
- После авторизации вы получите токен, который нужно будет указывать в заголовке запроса Authorization со значением: Token полученный_токен

- ***POST - запросы:***

-  Регистрация
- `http://127.0.0.1:8000/api/v1/book_market/registration/`
- В теле запроса указать username и password
- После успешного выполнения возвращается `{"status": "success"}`
-  Авторизация
- `http://127.0.0.1:8000/api/v1/book_market/auth_token/token/login`
- В теле запроса указать username и password
- После успешной авторизации вы получите токен `{"auth_token": "ваш_токен"}`
-  Выход
- `http://127.0.0.1:8000/api/v1/book_market/auth_token/token/logout`

**В следующих запросах необходимо указать заголовок запроса Authorization со значением: Token ваш_токен**

-  Формирование заявки на покупку:
`http://127.0.0.1:8000/api/v1/book_market/purchase_request/`
- В теле запроса указать book, user_phone и необязательное поле comment
- Если заявка сохранится успешно, то вернется ответ `{"status": "success"}`

- ***GET - запросы***

-  Список авторов
`http://127.0.0.1:8000/api/v1/book_market/authors/`
-  Список книг
`http://127.0.0.1:8000/api/v1/book_market/books/`

## Отправка почты администраторам
- Заполните поля своими данными в файле settings.py для отправки почты
- EMAIL_HOST_USER = '' # Ваша почта
- EMAIL_HOST_PASSWORD = '' # Ваш пароль
- DEFAULT_FROM_EMAIL = '' # Ваша почта
- DEFAULT_TO_EMAIL = '' # Ваша почта
- Для отправки электронной почты используется хост gmail. Вы можете поменять на свой, отредактировав строку:
- EMAIL_HOST = 'smtp.gmail.com'
