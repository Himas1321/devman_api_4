# Космический Телеграм

Набор скриптов загружает фотографии космической тематики в Telegram канал.

## Как установить
Скачайте репозиторий и установите Python пакеты из `requirements.txt`:
```bash
pip install -r requirements.txt
```
Для взаимодействия с API сервисов необходимо получить их API токены. Создайте в папке с проектом файл `.env` и добавляйте переменные с токенами в него, вот так:
```
TOKEN=<ваш токен>
TELEGRAM_TOKEN=<ваш телеграм токен>
TELEGRAM_CHAT_ID=<ваш чат айди>
PUBLISH_DELAY=<время публикации>
```
Какие переменные `.env` понадобятся:  
- TOKEN: токен NASA API необходимо получить на сайте [NASA API APOD](https://api.nasa.gov/#apod).
- TELEGRAM_TOKEN: необходимо получить в telegram у BotFather
- TELEGRAM_CHAT_ID: необходимо получить в telegram в вашем канале
- PUBLISH_DELAY: указать время публикации в секндах. Пример: 60 секунд * 60 минут = 3600 секунд это равно 1 часу 

## Основные скрипты

**fetch_space_x_images.py**  
Скачивает фото запуска ракет SpaceX с помощью [SpaceX API](https://github.com/r-spacex/SpaceX-API) Пример запуска:
```
python space_x.py
```

**fetch_nasa_apod_images.py**  
Скачивает фото на космическую тематику с сайта [NASA API APOD](https://api.nasa.gov/#apod).
Пример запуска:
```
python apod.py
```
**fetch_epic_images.py**  
Скачивает фото планеты Земля с сайта [NASA API EPIC](https://api.nasa.gov/#epic).
Пример запуска:
```
python epic.py
```
**telegram_bot.py**  
Запускает бота который публикует фото. Есть два способа
1 Публикует случайные фото с интервало указаным в PUBLISH_DELAY
Пример запуска:
```
python telegram_bot.py images
```
2 Публикует конкретное фото с интервало указаным в PUBLISH_DELAY
Пример запуска:
```
python telegram_bot.py images nasa_apod_1.jpg
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.