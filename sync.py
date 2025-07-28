import requests
import json
from datetime import datetime

API_SOURCE = "https://example.com/api/source"
API_TARGET = "https://example.com/api/target"

def fetch_employees():
    # Заглушка вместо реального запроса
    print("Получение данных из Системы-1")
    return [{"id": 1, "name": "Иван"}]

def transform(data):
    # Здесь можно изменить формат данных
    return data

def upload_to_target(data):
    # Заглушка вместо реального POST-запроса
    print(f"Отправка {len(data)} записей в Систему-2")

def sync():
    data = fetch_employees()
    transformed = transform(data)
    upload_to_target(transformed)
    print("Синхронизация завершена", datetime.now())

if __name__ == "__main__":
    sync()
