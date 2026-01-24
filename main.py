import os
from dotenv import load_dotenv
from image_download import download_images
from space_x import save_space_x_images
from apod import save_nasa_apod_images
from epic import save_epic_images


def main():
	load_dotenv()
	token = os.environ['TOKEN']
	save_space_x_images(token)
	save_nasa_apod_images(token)
	save_epic_images(token)

if __name__ == '__main__':
	main()
