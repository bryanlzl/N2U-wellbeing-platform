# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import telegram
import logging
import time

# Security clearance and login information for bot

NTU_MB_Bot = telegram.Bot(token = "1893158739:AAETldsJjkeMaQOVm6h_OTqB283Ubdq8Uy8")

# DEBUG: To get information about the NTU Mysterio(us) or whatever name box

print(NTU_MB_Bot.get_me()) 

# This class, which employs the telegram.ext.Dispatcher, provides a frontend to telegram.Bot to the programmer, so they can focus on coding the bot.
# Its purpose is to receive the updates from Telegram and to deliver them to said dispatcher.
# It also runs in a separate thread, so the user can interact with the bot, for example on the command line.
# The dispatcher supports handlers for different kinds of data: Updates from Telegram, basic text commands and even arbitrary types.
# The updater can be started as a polling service or, for production, use a webhook to receive updates. This is achieved using the WebhookServer and WebhookHandler classes.

from telegram.ext import Updater
NTU_MB_Bot_Updater = Updater(token = "1893158739:AAETldsJjkeMaQOVm6h_OTqB283Ubdq8Uy8", use_context = True)
NTU_MB_Bot_Dispatcher = NTU_MB_Bot_Updater.dispatcher

# Logging purposes and debugging in case of serious or fatal errors.

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Some lol function on start and all, along with experimenting on the handler function.

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Hello!\n\nThis is the NTU Mysterio Box initative, which seeks to enhance the well-being mindset, culture and practice on campus to bring wellbeing within NTU and the student population to the next level.")
    time.sleep(1)
    context.bot.send_message(chat_id = update.effective_chat.id, text = "⚠️ Disclaimer ⚠️\n\nPlease be aware that given the Well-being Hackathon 2021 and the development, this bot remains a work-in-progress. As such, certain key features or elements may not be available to you yet.")
    time.sleep(1)
    Introduction_Keyboard = [[telegram.InlineKeyboardButton("❓ What is NTU Mysterio Box?", callback_data = 'about_product')], [telegram.InlineKeyboardButton("📦 Order a box!", callback_data = 'order'), telegram.InlineKeyboardButton("📋 Order Status", callback_data = 'status')], [telegram.InlineKeyboardButton("🗳️ Suggestions", callback_data = 'suggestions'), telegram.InlineKeyboardButton("🤔 FAQs", callback_data = 'faq')], [telegram.InlineKeyboardButton("⛈️ How are you feeling today?", callback_data = 'emotional_check')]]
    Introduction_Markup = telegram.InlineKeyboardMarkup(Introduction_Keyboard)
    context.bot.send_message(chat_id = update.effective_chat.id, text = 'What would you like to inquire today?', reply_markup = Introduction_Markup)

# Need to make the bloody inline keyboard work la, fuck.
    
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
NTU_MB_Bot_Dispatcher.add_handler(start_handler)

# Another handler to listen in for regular messagesupdater.stop()
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
NTU_MB_Bot_Dispatcher.add_handler(echo_handler)

# Inititates the bot! To stop the bot, write NTU_MB_Bot_Updater.stop() into the command console prompt.
NTU_MB_Bot_Updater.start_polling()
