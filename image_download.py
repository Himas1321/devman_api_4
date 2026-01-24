import os
import requests

def download_images(full_path, item):
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
  }

  try:
    response = requests.get(item, headers=headers) 
    response.raise_for_status()

    with open(full_path, 'wb') as file:
      file.write(response.content)
    print("Файл скачан")

  except requests.exceptions.RequestException:
    print("Не удалось скачать")