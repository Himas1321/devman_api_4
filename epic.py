import os
import requests
from dotenv import load_dotenv
import urllib.parse
import datetime
from image_download import download_images

DEFAULT_PATH = 'image'


def fetch_epic_image_url(token):
  api_url = 'https://epic.gsfc.nasa.gov/api/natural'
  params = {
    'api_key': token,
  }

  response = requests.get(api_url, params=params)
  response.raise_for_status()
  epic_items = response.json()

  all_urls = []

  for epic_item in epic_items[:5]:
    image_name = epic_item['image']
    date = epic_item['date']

    date_part = datetime.datetime.fromisoformat(date)
    formatted_date = date_part.strftime("%Y/%m/%d")
    
    image_url = (
      f'https://api.nasa.gov/EPIC/archive/natural/'
      f'{formatted_date}/png/'
      f'{image_name}.png'
      f'?api_key={token}'
    )

    all_urls.append(image_url)

  return all_urls


def save_epic_images(token):
  epic_response = fetch_epic_image_url(token)

  if not os.path.exists(DEFAULT_PATH):
    os.makedirs(DEFAULT_PATH)

  for image_number, epic_url in enumerate(epic_response, start=1):
    parsed_url = urllib.parse.urlsplit(epic_url)
    directory, filename = os.path.split(parsed_url.path)
    name, file_extension  = os.path.splitext(filename)

    if not file_extension:
      continue
  
    filename = 'epic_' + str(image_number) + file_extension
    full_path = os.path.join(DEFAULT_PATH, filename)

    download_images(full_path, epic_url) 
    

def main():
  load_dotenv()
  token = os.environ['TOKEN']
  save_epic_images(token)


if __name__ == '__main__':
  main()