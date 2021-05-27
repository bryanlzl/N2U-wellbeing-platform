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

# Logging purposes and debugging in case of serious or fatal errors.

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Some lol function on start and all, along with experimenting on the handler function.

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Hello!\n\nThis is the NTU Mysterio Box initative, which seeks to enhance the well-being mindset, culture and practice on campus to bring wellbeing within NTU and the student population to the next level.")
    time.sleep(1)
    context.bot.send_message(chat_id = update.effective_chat.id, text = "⚠️ Disclaimer ⚠️\n\nPlease be aware that given the Well-being Hackathon 2021 and the development, this bot remains a work-in-progress. As such, certain key features or elements may not be available to you yet.")
    time.sleep(1)
    Introduction_Keyboard = [[telegram.InlineKeyboardButton("❓ What is NTU Mysterio Box?", callback_data = 'about_product')], 
                             [telegram.InlineKeyboardButton("📦 Order a box!", callback_data = 'order'), 
                              telegram.InlineKeyboardButton("📋 Order Status", callback_data = 'status')], 
                             [telegram.InlineKeyboardButton("🗳️ Suggestions", callback_data = 'suggestions'), 
                              telegram.InlineKeyboardButton("🤔 FAQs", callback_data = 'faq')], 
                             [telegram.InlineKeyboardButton("⛈️ How are you feeling today?", callback_data = 'emotional_check')]]
    Introduction_Markup = telegram.InlineKeyboardMarkup(Introduction_Keyboard)
    update.message.reply_text('What would you like to inquire today?', reply_markup = Introduction_Markup)

# Button function so that it is able to receive user input and respond accordingly.

def button(update, context):
    query = update.callback_query
    query.answer()
    
    #Try to make this algorithm nicer, since it is full of ifs and uses too much computational power. Chemistry student struggling here bro (and not specialized in this)
    if query.data == "start":
        Introduction_Keyboard = [[telegram.InlineKeyboardButton("❓ What is NTU Mysterio Box?", callback_data = 'about_product')], 
                                 [telegram.InlineKeyboardButton("📦 Order a box!", callback_data = 'order'), 
                                  telegram.InlineKeyboardButton("📋 Order Status", callback_data = 'status')], 
                                 [telegram.InlineKeyboardButton("🗳️ Suggestions", callback_data = 'suggestions'), 
                                  telegram.InlineKeyboardButton("🤔 FAQs", callback_data = 'faq')], 
                                 [telegram.InlineKeyboardButton("⛈️ How are you feeling today?", callback_data = 'emotional_check')]]
        Introduction_Markup = telegram.InlineKeyboardMarkup(Introduction_Keyboard)
        query.edit_message_text(text=f'What would you like to inquire today?', reply_markup = Introduction_Markup)
    elif query.data == "about_product":
        Return_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data = "start")]]
        Return_Markup = telegram.InlineKeyboardMarkup(Return_Keyboard)
        query.edit_message_text(text=f"❓ What is NTU Mysterio Box ❓\n\nThe NTU Mysterio Box is a well-being and mental wellness check that goes beyond online applications to give you a motivational box – a physical manifestation in which you will surely find useful in overcoming inconveniences while having it more personalized and tailored to your specific needs over time! Because here in NTU, every mental issue is unique, and we want to understand and help you to cope with life's mechanisms.\n\nDesigned by NTU students from various disciplines, we brought our different expertises into tackling this matter and hope that the NTU Mysterio Box will help to enhance the well-being and mindset of NTU students, all while ensuring that NTU remains a vibrant and conducive environment to work in.", reply_markup = Return_Markup)
    elif query.data == "faq":
        FAQ_Keyboard = [[telegram.InlineKeyboardButton("Price of the Mysterio Box", callback_data = "faq1")],
                        [telegram.InlineKeyboardButton("What to expect from the Mysterio Box?", callback_data = "faq2")],
                        [telegram.InlineKeyboardButton("Collection of Mysterio Box", callback_data = "faq3")], 
                        [telegram.InlineKeyboardButton("Delivery period of Mysterio Box", callback_data = "faq4")], 
                        [telegram.InlineKeyboardButton("I have more questions to ask! (Contact Admin)", callback_data = "faq_urgent")],
                        [telegram.InlineKeyboardButton("⬅️ Back", callback_data = "start")]]
        FAQ_Markup = telegram.InlineKeyboardMarkup(FAQ_Keyboard)
        query.edit_message_text(text=f"Frequently Asked Questions: To speak to an admin, do contact us here below!", reply_markup = FAQ_Markup)
    elif [query.data in "order", "status", "suggestions", "emotional_check"]:
        Return_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data = "start")]]
        Return_Markup = telegram.InlineKeyboardMarkup(Return_Keyboard)
        query.edit_message_text(text=f"Oops, this feature is still in developmental mode and we are unable to show it to you. Stay tuned!", reply_markup = Return_Markup)
        
    #query.edit_message_text(text=f"Selected option: {query.data}")
    
# Another handler to listen in for regular messagesupdater.stop()
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
# Just to collate everything.
    
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler
NTU_MB_Bot_Updater = Updater(token = "1893158739:AAETldsJjkeMaQOVm6h_OTqB283Ubdq8Uy8", use_context = True)
start_handler = CommandHandler('start', start)
NTU_MB_Bot_Dispatcher = NTU_MB_Bot_Updater.dispatcher
NTU_MB_Bot_Dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
NTU_MB_Bot_Dispatcher.add_handler(echo_handler)
NTU_MB_Bot_Dispatcher.add_handler(CallbackQueryHandler(button))

# Inititates the bot! To stop the bot, write NTU_MB_Bot_Updater.stop() into the command console prompt.
NTU_MB_Bot_Updater.start_polling()
