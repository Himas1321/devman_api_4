import os
import requests
import urllib.parse

def downloads_images(full_path, item):
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
  }

  response = requests.get(item, headers=headers) 
  response.raise_for_status()

  with open(full_path, 'wb') as file:
    file.write(response.content)
  print("Файл скачан")


def get_file_extension_from_url(url):
  parsed_url = urllib.parse.urlsplit(url)
  directory, filename = os.path.split(parsed_url.path)
  name, file_extension  = os.path.splitext(filename)
  return file_extension


