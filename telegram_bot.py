import telegram
import os
from dotenv import load_dotenv
load_dotenv()

bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
bot.send_message(text='Hi John!', chat_id='@nasa_telegram_bot1')

