# Human API

API разработано как тестовое задание для прохожения собеседования

## Развертывание

Для запуска необходим docker и docker-compose


```shell
git clone https://github.com/isz/humans-api.git
cd humans-api
./build.sh
docker-compose up -d
```

Сервис доступен по адресу
http://127.0.0.1:8080/api/human/


## Генерация тестовых данных

Необходима библиотека requests
```
pip install requests
```

Скрипт предполагает, что сервис находится на http://127.0.0.1:8080
Запуск скрипта
```
python fake/generate_data.py
```
Настройки генерации можно поправить в fake/generate_data.py
```python
COUNT = 500                         # count of data that will be generated
API_URL = "http://127.0.0.1:8080"   # service URL
```