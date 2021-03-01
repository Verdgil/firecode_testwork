## 1. Гуров Михаил
## 2. Тестовое задание: 
#### Цель: Реализовать сервис, который принимает и отвечает на HTTP запросы.
#### Функционал: 
   1. GET /city/ — получение всех городов из базы; 
   2. GET /city/city_id/street/ — получение всех улиц города; (city_id — идентификатор города)
   3. POST /shop/ — создание магазина; Данный метод получает json cобъектом магазина, в ответ возвращает id созданной записи. 
   4. GET /shop/?street=&city=&open=0/1 — получение списка магазин
## 3. Описание проекта: 
  Очень простенький бэкенд для тестово задания
## 4. Шаги по подготовке и установке:
0. Установить pyenv и зависимости для установки питона [`https://github.com/pyenv/pyenv/wiki#suggested-build-environment`](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
1. `pyenv install 3.9.1`
2. `pyenv local 3.9.1`
3. `pip install poetry`
4. `poetry install`
5. `poetry shell`
6. создать базу данных, и изменить под неё файл `firecode/settings.py.template`
7. скопировать его в `settings.py`
8. `./manage.py migrate`
9. создать админа `./manage.py createsuperuser`
10. Наслаждайтесь