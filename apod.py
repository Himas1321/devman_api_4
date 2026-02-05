import os
import requests
from dotenv import load_dotenv
import urllib.parse
from utilities import download_images, get_file_extension_from_url
import argparse

DEFAULT_PATH = 'images'

def fetch_nasa_apod_images_url(nasa_api_key, apod_count):
	api_url = "https://api.nasa.gov/planetary/apod"
	params = {
		"api_key": nasa_api_key,
		"count": apod_count
	}
	response = requests.get(api_url, params=params)
	response.raise_for_status()
	return response.json()


def get_apod_images(nasa_image_urls):
	images = []
	
	for image_number, nasa_url in enumerate(nasa_image_urls, start=1):
		decoded_url = urllib.parse.unquote(nasa_url['url'])
		file_extension = get_file_extension_from_url(decoded_url)

		if not file_extension:
			continue

		images.append((image_number, file_extension, decoded_url))

	return images


def save_nasa_apod_images(images):
	
	os.makedirs(DEFAULT_PATH, exist_ok=True)
	
	for image_number, file_extension, decoded_url in images:
		filename = f'nasa_apod_{image_number}{file_extension}'
		full_path = os.path.join(DEFAULT_PATH, filename)
		download_images(full_path, decoded_url)	


def create_parser():
	parser = argparse.ArgumentParser(
    description= 'Downloads NASA APOD images. Optionally specify number of images.'
    )
	parser.add_argument(
		'count',
		help='Number of images to download (default: 5)',
		nargs='?',
		default=5,
    	type=int,
	)

	return parser

def main():
	load_dotenv()

	nasa_api_key = os.environ['NASA_API_KEY']
	
	parser = create_parser()
	apod_count = parser.parse_args().count

	nasa_image_urls = fetch_nasa_apod_images_url(nasa_api_key, apod_count)
	images = get_apod_images(nasa_api_key, apod_count)
	save_nasa_apod_images(nasa_api_key, apod_count)

	
if __name__ == '__main__':
	main()
