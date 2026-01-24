import os
import requests
from dotenv import load_dotenv
import urllib.parse
from image_download import download_images

DEFAULT_PATH = 'image'


def fetch_nasa_apod(token):
	api_url = "https://api.nasa.gov/planetary/apod"
	params = {
		"api_key": token,
		"count": 20
	}
	response = requests.get(api_url, params=params)
	response.raise_for_status()
	return response.json()


def save_nasa_apod_images(token):
	nasa_response = fetch_nasa_apod(token)

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
	

def main():
	load_dotenv()
	demo_token = os.getenv('DEMO_KEY')
	token = os.environ['TOKEN']
	save_nasa_apod_images(token)


if __name__ == '__main__':
	main()