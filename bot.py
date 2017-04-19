#!/home/adam/miniconda3/envs/tBot/bin/python

print('before TG import')
import telegram
print('after TG import')

with open('tars.token', 'r') as f:
    tarsToken = f.readlines()[0].replace('\n', '')

#print(tarsToken)
bot = telegram.Bot(token=tarsToken)
print(bot.getMe())

from telegram.ext import Updater
updater = Updater(token=tarsToken)

# For quicker access to the Dispatcher used by your Updater, you can introduce it locally
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(bot, update):
     bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)



print('starting bot now...')
updater.start_polling()
