import os
import requests
from dotenv import load_dotenv
from utilities import downloads_images, get_file_extension_from_url
import argparse

DEFAULT_PATH = 'images'

def fetch_space_x_images_urls(space_x_launch_id):
	api_url = f'https://api.spacexdata.com/v5/launches/{space_x_launch_id}'
	response = requests.get(api_url)
	response.raise_for_status()
	launches = response.json()

	images = launches['links']['flickr']['original']

	return images

def get_space_x_images(space_x_image_urls):
	images = []

	for image_number, space_x_item in enumerate(space_x_image_urls, start=1):
		file_extension = get_file_extension_from_url(space_x_item)

		if not file_extension:
			continue

		images.append((image_number, file_extension, space_x_item))

	return images

def save_space_x_images(images):
	
	os.makedirs(DEFAULT_PATH, exist_ok=True)

	for image_number, file_extension, space_x_item in images:
		filename = f'space_x_{image_number}{file_extension}'
		full_path = os.path.join(DEFAULT_PATH, filename)
		downloads_images(full_path, space_x_item)


def create_parser():
	parser = argparse.ArgumentParser(
    description= 'The program downloads photos of Spacex launches by launch number (id).'
    )
	parser.add_argument(
		'launch_id',
		help='SpaceX launch ID (default: 5eb87d47ffd86e000604b38a)',
		nargs='?',
		type=str,
		default='5eb87d47ffd86e000604b38a',
	)
	return parser

def main():

	parser = create_parser()
	space_x_launch_id = parser.parse_args().launch_id

	space_x_image_urls = fetch_space_x_images_urls(space_x_launch_id)
	images = get_space_x_images(space_x_image_urls)
	save_space_x_images(images)
	

if __name__ == '__main__':
	main()