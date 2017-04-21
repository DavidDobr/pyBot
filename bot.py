# no shebang :
# # !/home/adam/miniconda3/envs/tBot/bin/python

# import https://github.com/python-telegram-bot
# you can use: conda install -c daviddobr python-telegram-bot=5.3.0
# urllib3 can be installed using: conda install -c daviddobr urllib3=1.20

# tutorial from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API

import telegram

tokenPath = '/home/adam/workspace/pyBot/tars.token'
with open(tokenPath, 'r') as f:
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

# Let's add another handler that listens for regular messages.
# Use the MessageHandler, another Handler subclass, to echo to all text messages:
def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)

# Note: As soon as you add new handlers to dispatcher, they are in effect.
dispatcher.add_handler(echo_handler)

def caps(bot, update, args):
    """echo user's message in all caps
    """
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

print('starting bot now...')
updater.start_polling()
