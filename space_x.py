import os
import requests
from dotenv import load_dotenv
import urllib.parse
from image_download import download_images

DEFAULT_PATH = 'image'


def fetch_space_x(token):
    api_url = 'https://api.spacexdata.com/v5/launches/5eb87d28ffd86e000604b373'
    response = requests.get(url)
    response.raise_for_status()
    launches = response.json()

    images = launches['links']['flickr']['original']

    return images

def save_space_x_images(token):
	space_x_response = fetch_space_x(token)

	if not os.path.exists(DEFAULT_PATH):
		os.makedirs(DEFAULT_PATH)

	for image_number, space_x_item in enumerate(space_x_response, start=1):
		parsed_url = urllib.parse.urlsplit(space_x_item)
		directory, filename = os.path.split(parsed_url.path)
		name, file_extension  = os.path.splitext(filename)

		if not file_extension:
			continue
	
		filename = 'space_x_' + str(image_number) + file_extension
		full_path = os.path.join(DEFAULT_PATH, filename)

		download_images(full_path, space_x_item)	


def main():
	load_dotenv()
	token = os.environ['TOKEN']
	save_space_x_images(token)


if __name__ == '__main__':
	main()