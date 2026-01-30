import os
import requests
from dotenv import load_dotenv
import urllib.parse
from image_download import download_images
import argparse

DEFAULT_PATH = 'images'


def fetch_nasa_apod(apod_count, token):
	if apod_count:
		parser_count = apod_count
	else:
		parser_count = '5'

	api_url = "https://api.nasa.gov/planetary/apod"
	params = {
		"api_key": token,
		"count": f'{parser_count}'
	}
	response = requests.get(api_url, params=params)
	response.raise_for_status()
	return response.json()


def save_nasa_apod_images(apod_count, token):
	nasa_response = fetch_nasa_apod(apod_count, token)

	if not os.path.exists(DEFAULT_PATH):
		os.makedirs(DEFAULT_PATH)

	for image_number, nasa_url in enumerate(nasa_response, start=1):
		decoded_url = urllib.parse.unquote(nasa_url['url'])
		
		parsed_url = urllib.parse.urlsplit(decoded_url)
		directory, filename = os.path.split(parsed_url.path)
		name, file_extension  = os.path.splitext(filename)

		if not file_extension:
			continue
	
		filename = 'nasa_apod_' + str(image_number) + file_extension
		full_path = os.path.join(DEFAULT_PATH, filename)

		download_images(full_path, decoded_url)	
	
def create_parser():
	parser = argparse.ArgumentParser(
    description= 'Downloads NASA APOD images. Optionally specify number of images.'
    )
	parser.add_argument(
		'count',
		help='count',
		nargs='?',
		type=int,
		default=None,
	)
	return parser

def main():
	load_dotenv()

	token = os.environ['TOKEN']

	parser = create_parser()
	apod_count = parser.parse_args().count
	
	save_nasa_apod_images(apod_count, token)


if __name__ == '__main__':
	main()