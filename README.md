# Система управления мероприятиями
Этот проект - представляет собой веб-приложение для управления мероприятиями и бронирования билетов.

## Установка

1. Клонируйте репозиторий на свой локальный компьютер:

```bash
git clone https://github.com/imangalikobey/event-management
```
2. Перейдите в каталог проекта

```bash
cd event-management
```
3. Установите зависимости

```bash
pip install -r requirements.txt
```
## Использование

1. Запустите flask приложение
```bash
python app.py
```
2. Перейдите в браузере по адресу 'http://127.0.0.1:5000/' для доступа к приложению.

## Процесс разработки

Этот проект разрабатывался с использованием Flask и Jinja2 для шаблонов HTML. Процесс разработки включал следующие этапы:

1. Проектирование: Определение функциональных требований и проектирование базовой архитектуры приложения.
2. Разработка: Создание основных компонентов приложения, таких как маршруты, модели базы данных, шаблоны HTML и формы.
3. Тестирование: Проверка функциональности и исправление ошибок.
4. Документация: Написание документации для кода и инструкций по установке.

## Уникальный подход
  Использовать библиотеку qrcode и сделать билет в виде qr-кода. 
## Компромисы и проблемы
1. Так как изначально данная вебприложение считалось мной не слишком тяжелой, backend framework-ом стал Flask, а не Django, но конец семестра чутька услосжнил разработку.
2. Был сделан шаблон HTML и добавлена база данных на SQLAlchemy, но из-за временных ограничений, та версия получилась слишком сыроватой и было решено отправить эту версию, где нет личного кабинета у пользователя.
3. Хотел сделать личный кабинет пользователя и админа(для CRUD) операций, но не хватило времени.
4. Из-за малого опыта в frontend, сделали сложной для создании .css с нуля, поэтому использовались готовые стили из bootstrap-a.
5. Множество багов при работе с sqlite и при создании логина и регистрации сбили темп разработки, они не были добавлены в эту версию. Но если они будут готовы к завтрешнему дню,то расположу другую версию и оставлю сюда ссылку...

Коротко о моем проекте
![alt text](https://i.kym-cdn.com/entries/icons/original/000/017/588/reality.jpg)

## Рефлексия

Спасибо, за возможность участвовать в вашем отборе!! Это был незабываемый опыт в разработке веб-приложений(не то что я люблю кодить)  с интересной темой.

POV: закончил документацию полностью в 01:08:
![alt text](https://i.kym-cdn.com/entries/icons/original/000/036/023/bale-1.jpg)
