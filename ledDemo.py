# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 13:26:28 2018

@author: zenofall.com
"""

import RPi.GPIO as GPIO

import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

updater = Updater(token='YOUR TOKEN GOES HERE') #This is where you enter token. 
#e.g. of a token: 412215502:AAJy2G0mwFHM7vj1v_y4iCH05EVbHrjIp6Q 
#updater = Updater(token='412215502:AAJy2G0mwFHM7vj1v_y4iCH05EVbHrjIp6Q ') 
#do not uncomment above lines, this is a made up token only for example. 
#please create your own bot and use your own token
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(bot, update):
     bot.send_message(chat_id=update.message.chat_id, text="Private Bot- Only responds to registered users!Bye...")
def led(bot, update,args):
    #print(args)    
    if(args[0]=='on'):
        bot.send_message(chat_id=update.message.chat_id, text="Led Is On")
        GPIO.output(4,GPIO.HIGH)
    if(args[0]=='off'):
        bot.send_message(chat_id=update.message.chat_id, text="Led Is Off")
        GPIO.output(4,GPIO.LOW)

            

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry Command Not Recognized!")            

def shutdown():
    updater.stop()
    updater.is_idle=False

def stop(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Stopping Server!")
    threading.Thread(target=shutdown).start()
    

      
start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)

ledHandler = CommandHandler('led',led, pass_args=True)
unknown_handler= MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(ledHandler)

dispatcher.add_handler(unknown_handler)


updater.start_polling()
updater.idle()

