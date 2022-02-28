Сервис s_test_rd.

Создан для сбора информации о репозиториях пользователей (проектов) github.com.

Сервису подается ссылка(список ссылок) на страницы пользователей(проектов). После чего сервис начинает сбор данных. Он 
переходит на страницу с репозиториями и начинает переходить по каждой ссылке репозитория собирая следующие данные (при 
наличии):
1. Название репозитория
2. Описание (About)
3. Ссылка на сайт
4. Количество звезд (stars)
5. Количество форков (forks)
6. Количество отслеживающих (watching)
7. Количество коммитов
8. Информация о последнем коммите
8.1. Автор
8.2. Название
8.3. Дата и время
9. Количество релизов
10. Информация о последнем релизе 
10.1. Версия
10.2. Дата и время создания
10.3. changelog

Информация по каждому репозиторию сохраняется в БД MongoDB.

Инструкция по использованию:

Сервис запускается через терминал командой - scrapy crawl spider_test

ВАЖНО! Перед запуском необходимо проверить запущен ли сервер MongoDB.

После запуска появится информация о необходимости ввести ссылки (Введите ссылки:).

Если ссылок более 1 то их необходимо вводить через запятую и пробел.

Пример: https://github.com/scrapy, https://github.com/celery/

