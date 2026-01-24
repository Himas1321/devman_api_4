## Как установить
Скачайте репозиторий и установите Python пакеты из `requirements.txt`:
```bash
pip install -r requirements.txt
```
Для взаимодействия с API сервисов необходимо получить их API токены. Создайте в папке с проектом файл `.env` и добавляйте переменные с токенами в него, вот так:
```
TOKEN=<ваш токен>
```
Какие переменные `.env` понадобятся:  
- TOKEN: токен NASA API необходимо получить на сайте [NASA API APOD](https://api.nasa.gov/#apod).

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

**main.py**  
Запускает все скрипты.
Пример запуска:
```
python main.py
```


## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.