import os
import requests
from dotenv import load_dotenv
import urllib.parse
from image_download import download_images
import argparse

DEFAULT_PATH = 'image'


def fetch_space_x(space_x_launch_id):
	if space_x_launch_id:
		api_url = f'https://api.spacexdata.com/v5/launches/{space_x_launch_id}'
	else:
		api_url = 'https://api.spacexdata.com/v5/latest'

	response = requests.get(api_url)
	response.raise_for_status()
	launches = response.json()

	images = launches['links']['flickr']['original']

	return images

def save_space_x_images(space_x_launch_id):
	space_x_response = fetch_space_x(space_x_launch_id)

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


def create_parser():
	parser = argparse.ArgumentParser(
    description= 'The program downloads photos of Spacex launches by launch number (id).'
    )
	parser.add_argument(
		'launch_id',
		help='launch ID',
		nargs='?',
		type=str,
		default=None,
	)
	return parser

def main():

	parser = create_parser()
	space_x_launch_id = parser.parse_args().launch_id

	save_space_x_images(space_x_launch_id)
	



if __name__ == '__main__':
	main()