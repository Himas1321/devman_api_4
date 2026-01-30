import os
import time
import random
import argparse
from dotenv import load_dotenv
import telegram


def publish_photos_forever(token, chat_id, delay, folder, photo_name):
    bot = telegram.Bot(token=token)

    while True:
        if photo_name:
            photo_path = os.path.join(folder, photo_name)

            with open(photo_path, "rb") as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)

            time.sleep(delay)
        else:   
            file_names = os.listdir(folder)
            random.shuffle(file_names)

            for file_name in file_names:
                with open(os.path.join(folder, file_name), "rb") as photo:
                    bot.send_photo(chat_id=chat_id, photo=photo)
                time.sleep(delay)


def create_parser():
    parser = argparse.ArgumentParser(
        description='Publish photos to Telegram channel with delay'
    )
    parser.add_argument(
        'image_dir',
        help='Directory with images',
    )
    parser.add_argument(
    'photo_name',
    nargs='?',
    help='Specific photo name'
    )
    return parser


def main():
    load_dotenv()

    parser = create_parser()
    args = parser.parse_args()

    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    delay = int(os.getenv('PUBLISH_DELAY'))

    publish_photos_forever(
        token, chat_id, 
        delay, folder=args.image_dir, 
        photo_name=args.photo_name
    )


if __name__ == '__main__':
    main()
