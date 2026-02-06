import os
import requests
from dotenv import load_dotenv
import urllib.parse
import datetime
from utilities import downloads_images, get_file_extension_from_url

DEFAULT_PATH = 'images'
EPIC_IMAGES_LIMIT = 5

def fetch_epic_images_urls(nasa_api_key):
  api_url = 'https://epic.gsfc.nasa.gov/api/natural'
  params = {
    'api_key': nasa_api_key,
  }

  response = requests.get(api_url, params=params)
  response.raise_for_status()
  epic_items = response.json()

  all_urls = []

  for epic_item in epic_items[:EPIC_IMAGES_LIMIT]:
    image_name = epic_item['image']
    date = epic_item['date']

    date_part = datetime.datetime.fromisoformat(date)
    formatted_date = date_part.strftime("%Y/%m/%d")
    
    image_url = (
      f'https://api.nasa.gov/EPIC/archive/natural/'
      f'{formatted_date}/png/'
      f'{image_name}.png'
      f'?api_key={nasa_api_key}'
    )

    all_urls.append(image_url)

  return all_urls


def save_epic_images(epic_image_urls):
  os.makedirs(DEFAULT_PATH, exist_ok=True)

  for image_number, epic_url in enumerate(epic_image_urls, start=1):
    file_extension = get_file_extension_from_url(epic_url)

    if not file_extension:
      continue

    images.append((image_number, file_extension, epic_url))
  
    filename = f'epic_{image_number}{file_extension}'
    full_path = os.path.join(DEFAULT_PATH, filename)
    downloads_images(full_path, epic_url) 
    

def main():
  load_dotenv()

  nasa_api_key = os.environ['NASA_API_KEY']
  
  epic_image_urls = fetch_epic_images_urls(nasa_api_key)
  save_epic_images(epic_image_urls)


if __name__ == '__main__':
  main()