#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:50:31 2021

@author: tuweile
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import telegram
import logging
import time
import asyncio

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, ShippingOption, LabeledPrice
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler,
    ShippingQueryHandler,
    PreCheckoutQueryHandler
)

# Security clearance and login information for bot

NTU_MB_Bot = telegram.Bot(token="1893158739:AAETldsJjkeMaQOVm6h_OTqB283Ubdq8Uy8")
logger = logging.getLogger(__name__)
DELIVERY, LOCATION, SUBSCRIPTION, CONFIRMATION, SAVEINFO, CLOSED = range(6)

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

def start(update: Update, _: CallbackContext):
    update.message.reply_text(
        "Hello!\n\nThis is the NTU Mysterio Box initative, which seeks to enhance the well-being mindset, culture and practice on campus to bring wellbeing within NTU and the student population to the next level.")
    time.sleep(1)
    update.message.reply_text(
        "⚠️ <b>Disclaimer</b> ⚠️\n\nPlease be aware that given the Well-being Hackathon 2021 and the development, this bot remains a work-in-progress. As such, certain key features or elements may not be available to you yet.",
        parse_mode=telegram.ParseMode.HTML)
    time.sleep(1)
    Introduction_Keyboard = [
        [telegram.InlineKeyboardButton("❓ What is NTU Mysterio Box?", callback_data='about_product')],
        [telegram.InlineKeyboardButton("📦 Order a box!", callback_data='order'),
         telegram.InlineKeyboardButton("📋 Order Status", callback_data='status')],
        [telegram.InlineKeyboardButton("🗳️ Suggestions", callback_data='suggestions'),
         telegram.InlineKeyboardButton("🤔 FAQs", callback_data='faq')],
        [telegram.InlineKeyboardButton("⛈️ How are you feeling today?", callback_data='emotional_check')]]
    Introduction_Markup = telegram.InlineKeyboardMarkup(Introduction_Keyboard)
    update.message.reply_text('What would you like to inquire today?', reply_markup=Introduction_Markup)


def adminbutton(update: Update, _: CallbackContext):
    adminquery = update.callback_query
    adminquery.answer()
    # Try to make this algorithm nicer, since it is full of ifs and uses too much computational power. Chemistry student struggling here bro (and not specialized in this)
    if adminquery.data == "console":
        admin_Keyboard = [
            [telegram.InlineKeyboardButton("New poll", callback_data='poll')]]
        admin_Markup = telegram.InlineKeyboardMarkup(admin_Keyboard)
        query.edit_message_text(text=f'Admin Panel', reply_markup=admin_Markup)


def admin(update: Update, _: CallbackContext):
    admin_list = [195612849, 214053283, 270308503, 125308490, 193865641]
    adminquery = update.callback_query
    user = update.message.from_user
    if user.id in admin_list:
        admin_Keyboard = [
            [telegram.InlineKeyboardButton("Create Feedback Form", callback_data = 'feedback')]]
        admin_Markup = telegram.InlineKeyboardMarkup(admin_Keyboard)
        update.message.reply_text(text=f'Admin Panel', reply_markup=admin_Markup)
    else:
        return

# Button function so that it is able to receive user input and respond accordingly.

def button(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()

    # Try to make this algorithm nicer, since it is full of ifs and uses too much computational power. Chemistry student struggling here bro (and not specialized in this)
    if query.data == "start":
        Introduction_Keyboard = [
            [telegram.InlineKeyboardButton("❓ What is NTU Mysterio Box?", callback_data='about_product')],
            [telegram.InlineKeyboardButton("📦 Order a box!", callback_data='order'),
             telegram.InlineKeyboardButton("📋 Order Status", callback_data='status')],
            [telegram.InlineKeyboardButton("🗳️ Suggestions", callback_data='suggestions'),
             telegram.InlineKeyboardButton("🤔 FAQs", callback_data='faq')],
            [telegram.InlineKeyboardButton("⛈️ How are you feeling today?", callback_data='emotional_check')]]
        Introduction_Markup = telegram.InlineKeyboardMarkup(Introduction_Keyboard)
        query.edit_message_text(text=f'What would you like to inquire today?', reply_markup=Introduction_Markup)
    elif query.data == "about_product":
        Return_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data="start")]]
        Return_Markup = telegram.InlineKeyboardMarkup(Return_Keyboard)
        query.edit_message_text(
            text=f"❓<b> What is NTU Mysterio Box </b>❓\n\nThe NTU Mysterio Box is a well-being and mental wellness check that goes beyond online applications to give you a motivational box – a physical manifestation in which you will surely find it useful in overcoming inconveniences while having it tailored and personalized to your own specific needs over time! Because here in NTU, every mental issue is unique, and we want to understand and help you to cope with life's mechanisms.\n\nDesigned by NTU students from various disciplines, we brought our different expertises into tackling this matter and hope that the NTU Mysterio Box will help to enhance the well-being and mindset of NTU students, all while ensuring that NTU remains a vibrant and conducive environment to work in.",
            reply_markup=Return_Markup, parse_mode=telegram.ParseMode.HTML)
    elif query.data == "faq":
        FAQ_Keyboard = [[telegram.InlineKeyboardButton("Price of the Mysterio Box", callback_data="faq1")],
                        [telegram.InlineKeyboardButton("What to expect from the Mysterio Box?", callback_data="faq2")],
                        [telegram.InlineKeyboardButton("Collection of Mysterio Box", callback_data="faq3")],
                        [telegram.InlineKeyboardButton("Delivery period of Mysterio Box", callback_data="faq4")],
                        [telegram.InlineKeyboardButton("I have more questions to ask! (Contact Admin)",
                                                       callback_data="faq_urgent")],
                        [telegram.InlineKeyboardButton("⬅️ Back", callback_data="start")]]
        FAQ_Markup = telegram.InlineKeyboardMarkup(FAQ_Keyboard)
        query.edit_message_text(text=f"Frequently Asked Questions: To speak to an admin, do contact us here below!",
                                reply_markup=FAQ_Markup)

    if query.data == "order":
        OrderP1_Keyboard = [[telegram.InlineKeyboardButton("General Box", callback_data="order_generic")],
                            [telegram.InlineKeyboardButton("Personalized Box (Not Available)",
                                                           callback_data="order_personalized")],
                            [telegram.InlineKeyboardButton("⬅️ Back", callback_data="start")]]
        OrderP1_Markup = telegram.InlineKeyboardMarkup(OrderP1_Keyboard)
        query.edit_message_text(
            text=f"Great! What kind of box would you like to get for yourself?\n\nPlease be aware that the personalized box is still currently under development.",
            reply_markup=OrderP1_Markup)
    elif query.data == "order_generic":
        OrderP2G_Keyboard = [[telegram.InlineKeyboardButton("Box A", callback_data="order_generic_A")],
                             [telegram.InlineKeyboardButton("Box B", callback_data="order_generic_B")],
                             [telegram.InlineKeyboardButton("What's inside this month's boxes?",
                                                            callback_data="order_generic_query")],
                             [telegram.InlineKeyboardButton("⬅️ Back", callback_data="order")]]
        OrderP2G_Markup = telegram.InlineKeyboardMarkup(OrderP2G_Keyboard)
        query.edit_message_text(
            text=f"Fantastic choice. What boxes would you be interested in getting for this month, or do you need more info?",
            reply_markup=OrderP2G_Markup)
    elif query.data == "order_generic_A":
        OrderP3_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data="order_generic")]]
        OrderP3_Markup = telegram.InlineKeyboardMarkup(OrderP3_Keyboard)
        query.edit_message_text(
            text=f"Awesome! To confirm, please click or use the command /boxA to begin your transaction!",
            reply_markup=OrderP3_Markup)
        return ConversationHandler
    elif query.data == "order_generic_B":
        OrderP3_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data="order_generic")]]
        OrderP3_Markup = telegram.InlineKeyboardMarkup(OrderP3_Keyboard)
        query.edit_message_text(
            text=f"Awesome! To confirm, please click or use the command /boxB to begin your transaction!",
            reply_markup=OrderP3_Markup)
    elif query.data == "order_generic_query":
        OrderP3_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data="order_generic")]]
        OrderP3_Markup = telegram.InlineKeyboardMarkup(OrderP3_Keyboard)
        query.edit_message_text(
            text=f"For this month's boxes, this is what you can expect to receive:\n\n<b>Box A :</b> Placeholder\n\n<b>Box B: </b> Placeholder",
            reply_markup=OrderP3_Markup, parse_mode=telegram.ParseMode.HTML)

    if query.data == "suggestions":
        SuggestionsHP_Keyboard = [
            [telegram.InlineKeyboardButton("Next Month Item Poll Nominations", callback_data="suggestions_itempoll")],
            [telegram.InlineKeyboardButton("📞 Resources and Hotlines", callback_data="suggestions_resources")],
            [telegram.InlineKeyboardButton("I have a suggestion! (Contact Admin)", callback_data="suggestions_admin")],
            [telegram.InlineKeyboardButton("⬅️ Back", callback_data="start")]]
        SuggestionsHP_Markup = telegram.InlineKeyboardMarkup(SuggestionsHP_Keyboard)
        query.edit_message_text(
            text=f"Nice, we always appreciate your suggestions and your feedback! What would you like to discuss about?",
            reply_markup=SuggestionsHP_Markup)
    # Item Poll and Feedback Poll
    elif query.data == "suggestions_resources":
        SuggestionsHPR_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data="suggestions")]]
        SuggestionsHPR_Markup = telegram.InlineKeyboardMarkup(SuggestionsHPR_Keyboard)
        query.edit_message_text(
            text=f"<b>📞 Resources and Hotlines</b>\n\nNTU continues to support and empower students to take positive action through its various services.\n\n<b>NTU Counselling Centre (UCC)</b>\nBook an appointment: https://bit.ly/3cExnEN \n☎ Office Hours: +65 6790 4462\n☎ After-office Hours <i>(emergency only)</i>: +65 6904 7041\n📩 E-mail: ucc-students@ntu.edu.sg\n\n<b>Operating Hours</b>\nMonday - Thursday: 8:30am to 5:45pm\nFriday: 8:30am to 5:15pm\nWeekends and PH: Closed\n\n<b>External Resources</b>\n<i>SHINE Children & Youth Services</i>\n📱 WhatsApp: 8788 3171\n📩 E-mail: resilience@shine.org.sg \nWebsite: https://www.shine.org.sg/resilience",
            reply_markup=SuggestionsHPR_Markup, parse_mode=telegram.ParseMode.HTML)
    elif query.data == "suggestions_admin":
        SuggestionsHPR_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data="suggestions")]]
        SuggestionsHPR_Markup = telegram.InlineKeyboardMarkup(SuggestionsHPR_Keyboard)
        query.edit_message_text(
            text=f"Fantastic! We would love to get your feedback on our services in Telegram! Please do leave your suggestions and recommendations here with the command /feedback (message)\n\n<i>Please be aware that our administrators may contact you via Telegram to inquire about your suggestions where possible.</i>",
            reply_markup=SuggestionsHPR_Markup, parse_mode=telegram.ParseMode.HTML)

    if query.data == "faq1":
        Return_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data="faq")]]
        Return_Markup = telegram.InlineKeyboardMarkup(Return_Keyboard)
        query.edit_message_text(text=f"Placeholder here.", reply_markup=Return_Markup)
    elif query.data == "faq2":
        Return_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data="faq")]]
        Return_Markup = telegram.InlineKeyboardMarkup(Return_Keyboard)
        query.edit_message_text(text=f"Placeholder here.", reply_markup=Return_Markup)
    elif query.data == "faq3":
        Return_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data="faq")]]
        Return_Markup = telegram.InlineKeyboardMarkup(Return_Keyboard)
        query.edit_message_text(text=f"Placeholder here.", reply_markup=Return_Markup)
    elif query.data == "faq4":
        Return_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data="faq")]]
        Return_Markup = telegram.InlineKeyboardMarkup(Return_Keyboard)
        query.edit_message_text(text=f"Placeholder here.", reply_markup=Return_Markup)
    elif query.data == "faq_urgent":
        Return_Keyboard = [[telegram.InlineKeyboardButton("⬅️ Back", callback_data="faq")]]
        Return_Markup = telegram.InlineKeyboardMarkup(Return_Keyboard)
        query.edit_message_text(
            text=f"No worries! We will get back to you at the best possible arrangement and time through Telegram! Please do leave your inquiries here with the command /faq <message>.",
            reply_markup=Return_Markup)

    # query.edit_message_text(text=f"Selected option: {query.data}")


# Another handler to listen in for regular messagesupdater.stop()
# def echo(update, context):
#    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
#    print(update.message.text)

# So the first ConversationHandler
# def feedback(update: Update, _: CallbackContext):
#     message = update.message.text
#     query = update.callback_query
#     print("hello world!")
#     print(message)

#     if query.data == "faq_urgent":
#         print("hello world")

# Lazy to make a proper conversation handler, because it seems consecutive and does not allow for going back to previous conversations. Command handlers are easier.
def command_faq(update: Update, _: CallbackContext):
    user = update.message.from_user
        
    # This message is only if nothing has been inputted inside the command.
    if update.message.text == "/faq":
        update.message.reply_text("Please enter your FAQ question down below, and we will get back to you at the best possible arrangement and time through Telegram!\n\nThe correct format is: /faq <message>")
        
    elif update.message.from_user.is_bot == True:
        update.message.reply_text("Hello bot! Unfortunately to prevent spam, all automated bot messages will not be processed accordingly. Please use a non-bot account to proceed with this.")
        
    else:
        update.message.reply_text("✅ <b>Your inquiry has been received.</b> ✅\n\nThank you for your inquiry! We will be messaging you back on Telegram shortly to address your question. You will now be re-directed to the starting page.", parse_mode = telegram.ParseMode.HTML)
        time.sleep(1)
        _.bot.sendSticker(chat_id = user.id, sticker = "CAACAgIAAxkBAAECbQVgxmOXGKQiXaJuivCoKJEOBi3q0AAC_gADVp29CtoEYTAu-df_HwQ")
        message = update.message.text.partition("/faq ")[2]
        _.bot.send_message(chat_id = -1001389088902, text = "✋ <b>FAQ Inquiry Received!</b> ✋\n\nName: " + str(user.first_name) + " " + str(user.last_name) + "\n\nUsername: @" + str(user.username) + "\n\nMessage: " + str(message) + "\n\n<i>This user requires assistance. Please reply back to this user immediately to resolve the problem.</i>", parse_mode = telegram.ParseMode.HTML)
        time.sleep(3)
        return start(update, _)

def command_feedback(update: Update, _: CallbackContext):
    user = update.message.from_user
    
    if update.message.text == "/feedback":
        update.message.reply_text("Please enter your feedback down below, and we will get back to you at the best possible arrangement and time through Telegram!\n\nThe correct format is: /feedback <message>")
    
    elif update.message.from_user.is_bot == True:
        update.message.reply_text("Hello bot! Unfortunately to prevent spam, all automated bot messages will not be processed accordingly. Please use a non-bot account to proceed with this.")
        
    else:
        update.message.reply_text("✅ <b>Your inquiry has been received.</b> ✅\n\nThank you for your inquiry! We will be messaging you back on Telegram shortly to address your question. You will now be re-directed to the starting page.", parse_mode = telegram.ParseMode.HTML)
        time.sleep(1)
        _.bot.sendSticker(chat_id = user.id, sticker = "CAACAgIAAxkBAAECbaRgx2csR9SjmsXnCqAIQkXBAAFmLFkAAkgCAAJWnb0KHPVy-NwpFNAfBA")
        message = update.message.text.partition("/feedback ")[2]
        _.bot.send_message(chat_id = -1001268756108, text = "💬 <b>Feedback Inquiry Received!</b> 💬\n\nName: " + str(user.first_name) + " " + str(user.last_name) + "\n\nUsername: @" + str(user.username) + "\n\nMessage: " + str(message) + "\n\n<i>This user has submitted feedback. Do review the feedback, discuss with fellow administrators and reply back to the user where necessary for clarification.</i>", parse_mode = telegram.ParseMode.HTML)
        time.sleep(3)
        return start(update, _)


def command_TelegramboxA(update: Update, _: CallbackContext):
    user = update.message.from_user

    SwiftBoxA = LabeledPrice("NTU Mysterio Box A", 600)
    _.bot.sendInvoice(chat_id=user.id, title="NTU Mysterio Box A",
                      description="A motivational box for students (Placeholder)", payload="swiftboxA",
                      provider_token="284685063:TEST:YWI4MTZhMmY3ZjYz", currency="SGD", prices=[SwiftBoxA],
                      max_tip_amount=500, suggested_tip_amounts=[50, 100, 200, 500],
                      photo_url="https://i3.cpcache.com/product/1813695916/powerful_inspirational_quote_keepsake_box.jpg?side=Front&color=Mahogany&height=630&width=630&qv=90",
                      photo_size=200, photo_width=200, photo_height=200, need_name=True, need_phone_number=True,
                      need_email=True, need_shipping_address=True, send_phone_number_to_provider=True,
                      send_email_to_provider=True, is_flexible=True)


def command_TelegramboxB(update: Update, _: CallbackContext):
    user = update.message.from_user

    SwiftBoxA = LabeledPrice("NTU Mysterio Box B", 600)
    _.bot.sendInvoice(chat_id=user.id, title="NTU Mysterio Box B",
                      description="A motivational box for students (Placeholder)", payload="swiftboxB",
                      provider_token="284685063:TEST:YWI4MTZhMmY3ZjYz", currency="SGD", prices=[SwiftBoxA],
                      max_tip_amount=500, suggested_tip_amounts=[50, 100, 200, 500],
                      photo_url="https://i3.cpcache.com/product/1813695916/powerful_inspirational_quote_keepsake_box.jpg?side=Front&color=Mahogany&height=630&width=630&qv=90",
                      photo_size=200, photo_width=200, photo_height=200, need_name=True, need_phone_number=True,
                      need_email=True, need_shipping_address=True, send_phone_number_to_provider=True,
                      send_email_to_provider=True, is_flexible=True)


def command_Telgrambox_shippingquery(update: Update, _: CallbackContext) -> None:
    query = update.shipping_query
    payload_query = ["swiftboxA", "swiftboxB"]

    try:
        if ((query.invoice_payload in payload_query) == False):
            query.answer(ok=False,
                         error_message="\nAn authentication error has occurred during the transaction.\n\nYour payment has not been charged, please restart the transaction and contact the administrators via /faq immediately.")
            return
        elif query.shipping_address.country_code != "SG":
            query.answer(ok=False,
                         error_message="\nAt the present moment, we only accept deliveries to local Singapore addresses! Please consider a local Singapore address with the correct postal code.\n\nYour payment has not been charged.")
            return
        elif len(query.shipping_address.post_code) != 6:
            query.answer(ok=False,
                         error_message="\nAn invalid postal code has been entered. Please verify your 6-digit postal code again before submitting.\n\nYour payment has not been charged.")
            return
        elif (int(query.shipping_address.post_code)):
            pass
        elif query.from_user.is_bot == True:
            query.answer(ok=False,
                         error_message="\nError 404.\n\nFORCED QUERY: Are you a robot? If boolean is set to TRUE, terminate immediately.")
            return
    except ValueError:
        query.answer(ok=False,
                     error_message="\nYou have entered an invalid postal code. Please verify the postal code again before submitting.\n\nYour payment has not been charged.")
        return

    # First option has a single LabeledPrice
    options = [ShippingOption('1', 'Self Collection', [LabeledPrice('Self Collection', 0)]),
               ShippingOption('2', 'Mail-In Delivery', [LabeledPrice('Mail-In Delivery', 150)])]
    # second option has an array of LabeledPrice objects
    # price_list = [LabeledPrice('B1', 150), LabeledPrice('B2', 200)]
    # options.append(ShippingOption('2', 'Shipping Option B', price_list))
    query.answer(ok=True, shipping_options=options)


def command_Telgrambox_precheckoutquery(update: Update, _: CallbackContext) -> None:
    query = update.pre_checkout_query
    payload_query = ["swiftboxA", "swiftboxB"]

    if ((query.invoice_payload in payload_query) == False):
        query.answer(ok=False,
                     error_message="\nAn authentication error has occurred during the transaction.\n\nYour payment has not been charged, please restart the transaction and contact the administrators via /faq immediately.")
        return
    if query.currency != "SGD":
        query.answer(ok=False,
                     error_message="\nAt the present moment, we only accept local Singapore currencies denominated in SGD. Please use a payment method that accepts SGD.\n\nYour payment has not been charged.")
        return
    elif query.from_user.is_bot == True:
        query.answer(ok=False,
                     error_message="\nError 404.\n\nFORCED QUERY: Are you a robot? If boolean is set to TRUE, terminate immediately.")
        return
    else:
        query.answer(ok=True)


def command_Telgrambox_successfulpayment(update: Update, _: CallbackContext) -> None:
    user = update.message.from_user
    # need to include a reference system
    update.message.reply_text(
        "✅ <b>Your payment has been received.</b> ✅\n\nThank you so much for using N2U! Your order status referral code is <b>XXX-XXX</b>.\n\nPlease save this message for your future references. If you have any inquiries, refunds or issues, please use the /faq command and we will reply back to you at the best arrangement!\n\n<i>Our terms and conditions can be found here.</i>\n\nYou will now be redirected back to our home page.",
        parse_mode=telegram.ParseMode.HTML)
    time.sleep(1)
    _.bot.sendSticker(chat_id=user.id,
                      sticker="CAACAgIAAxkBAAECbQFgxmHwbT1Nt_3oEwHHqwbwcwQ31wACBwEAAladvQq_tyZhIpO5oh8E")
    time.sleep(5)
    return start(update, _)


# def command_boxA(update: Update, _: CallbackContext) -> int:
#     update.message.reply_text(
#         '<i>How many Box A would you like to order? Please give a number!</i>\n\n'
#         '<i>At any point you would like to close the transaction, please use /cancel.</i>\n'
#         '<i>The price for one Mysterio Box A is S$5.</i>', parse_mode = telegram.ParseMode.HTML
#     )
#     return DELIVERY

# def delivery(update: Update, _: CallbackContext) -> int:
#     user = update.message.from_user
#     message = update.message.text #need to take the amt.

#     if user.is_bot == True:
#         update.message.reply_text(
#             "Beep boop. I am sorry, but we do not process bot orders or messages at the time. Please use a real (and human) account to do this."
#             )

#     try:
#         if message == "/cancel":
#             return cancel(update, _)

#         elif int(message) <= 0:
#             update.message.reply_text(
#             "<i>Sorry, but we are unable to process the quantity you have given us. Please try again.</i>", parse_mode = telegram.ParseMode.HTML
#             )
#             time.sleep(1)
#             return command_boxA(update, _)

#         elif int(message) > 3:
#             update.message.reply_text(
#                 "That's a lot! Just to clarify, you are ordering " + str(message) + " boxes! If this was a mistake, please /cancel your order!"
#                 )
#             time.sleep(1)

#         else:
#             pass

#     except:
#         update.message.reply_text(
#             "<i>Sorry, but you will need to key in a <b>proper number</b> of boxes you would like to order!</i>", parse_mode = telegram.ParseMode.HTML
#             )
#         time.sleep(1)
#         return command_boxA(update, _)

#     order_1quantity = int(message)

#     delivery_keyboard = [["Self-collection", "Mail-in"]]

#     update.message.reply_text("<i>How about delivery method? Would you prefer to self-collect at the designated venues or to do a mail-in delivery?</i>",
#                               reply_markup = ReplyKeyboardMarkup(delivery_keyboard, one_time_keyboard = True), parse_mode = telegram.ParseMode.HTML)
#     return LOCATION

# def location(update: Update, _: CallbackContext) -> int:
#     message = update.message.text #grab the delivery method

#     update.message.reply_text(
#         "<i>Awesome! Please enter your full address along with your postal code (especially for mail-in) so that we can send it on your way!\n\nIf you accidentally typed in the wrong address, that's alright – you can simply /cancel.</i>", reply_markup=ReplyKeyboardRemove(), parse_mode = telegram.ParseMode.HTML)

#     order_2delivery = message

#     return SUBSCRIPTION

# def subscription(update: Update, _: CallbackContext) -> int:
#     user = update.message.from_user
#     message = update.message.text #grab the location

#     subscription_keyboard = [["One-time", "Monthly Subscription"]]

#     order_3address = message

#     update.message.reply_text(
#         "<i>Great! Just to ask, would you like to make this a monthly subscription (and be surprised with our monthly boxes) or just an one-off thing?</i>", parse_mode = telegram.ParseMode.HTML,
#         reply_markup=ReplyKeyboardMarkup(subscription_keyboard, one_time_keyboard = True
#         ))
#     return CONFIRMATION

# def boxA_confirmation(update: Update, _: CallbackContext) -> int:
#     user = update.message.from_user
#     message = update.message.text #grab the subscription

#     confirmation_keyboard = [["Yes", "No"]]

#     order_4subscription = message

#     update.message.reply_text(
#         "<i>Alright! So just to confirm, you will be ordering (TBA-qty) Box A via (TBA-mode) to this address (TBA-address) under a (TBA-mode) basis.\n\nPlease verify whether is this correct!</i>", parse_mode = telegram.ParseMode.HTML,
#         reply_markup = ReplyKeyboardMarkup(confirmation_keyboard, one_time_keyboard=True))
#     return SAVEINFO

# def saveinfo(update: Update, _: CallbackContext) -> int:
#     user = update.message.from_user
#     message = update.message.text

#     if message == "No":
#         update.message.reply_text(
#             "<i>Your order has not been processed due to payment failure. Please /start the bot again to begin.</i>", reply_markup=ReplyKeyboardRemove(), parse_mode = telegram.ParseMode.HTML)
#         time.sleep(1)
#         return ConversationHandler.END, start(update, _)

#     confirmation_keyboard = [["Yes", "No"]]

#     update.message.reply_text(
#         "<i>Done! Would you like us to save your location for future use?</i>", parse_mode = telegram.ParseMode.HTML,
#         reply_markup = ReplyKeyboardMarkup(confirmation_keyboard, one_time_keyboard=True))
#     return CLOSED

#     #TODO:
#         #1. Grab the data and store it in persistence to refer back where necessary.
#         #2. Use the Telegram API to make payments and all, preferably with DBS PayLah / PayNow.
#         #3. Figure a way to confirm and collate orders.

# def closed(update: Update, _: CallbackContext) -> int:
#     user = update.message.from_user
#     message = update.message.text

#     update.message.reply_text(
#         "✅ <b>Your order has been received.</b> ✅\n\n<i>Thank you for your payment, your order will now be processed accordingly. Your order referral code is: (Referral-code-TBA).</i>\n\n<i>If you have any inquiries to your order, please do not hestitate to leave a support ticket in FAQ!</i>", reply_markup=ReplyKeyboardRemove(), parse_mode = telegram.ParseMode.HTML)
#     time.sleep(3)
#     return ConversationHandler.END, start(update, _)

# def cancel(update: Update, _: CallbackContext) -> int:
#     user = update.message.from_user
#     logger.info("User %s canceled the conversation.", user.first_name)
#     update.message.reply_text(
#         'You have cancelled the transaction. Please /start the bot again to begin.', reply_markup=ReplyKeyboardRemove(), parse_mode = telegram.ParseMode.HTML
#     )
#     time.sleep(1)

#     return ConversationHandler.END, start(update, _)

# Weak cancel function just to meet conv_handler requirements
# def cancel(update: Update, _: CallbackContext):
#     update.message.reply_text('Bye! I hope we can talk again some day.')

# Just to collate everything.
# def facts_to_str(user_data: Dict[str, str]) -> str:
#     """Helper function for formatting the gathered user info."""
#     facts = [f'{key} - {value}' for key, value in user_data.items()]
#     return "\n".join(facts).join(['\n', '\n'])

def main() -> None:
    #    pers_data = PicklePersistence(filename = "N2U_purchasebot")

    # conv_handler = ConversationHandler(
    #     entry_points=[CommandHandler('boxA', command_boxA)],
    #     states={
    #         DELIVERY: [MessageHandler(Filters.text, delivery), CommandHandler('cancel', cancel)],
    #         LOCATION: [MessageHandler(Filters.text('^(Self-collection|Mail-in)$'), location),CommandHandler('cancel', cancel)],
    #         SUBSCRIPTION: [MessageHandler(Filters.text, subscription), CommandHandler('cancel', cancel)],
    #         CONFIRMATION: [MessageHandler(Filters.text('^(One-time|Monthly Subscription)$'), boxA_confirmation), CommandHandler('cancel', cancel)],
    #         SAVEINFO: [MessageHandler(Filters.text('^(Yes|No)$'), closed)],
    #         CLOSED: [MessageHandler(Filters.text('^(Yes|No)$'), closed)]
    #     },
    #     fallbacks=[CommandHandler('cancel', cancel)],
    #     allow_reentry = True,
    # )

    NTU_MB_Bot_Updater = Updater(token="1893158739:AAETldsJjkeMaQOVm6h_OTqB283Ubdq8Uy8", use_context=True)
    # start_handler = CommandHandler('start', start)
    # cancel_handler = CommandHandler('cancel', cancel)
    NTU_MB_Bot_Dispatcher = NTU_MB_Bot_Updater.dispatcher
    NTU_MB_Bot_Dispatcher.add_handler(CommandHandler('start', start))
    NTU_MB_Bot_Dispatcher.add_handler(CommandHandler('faq', command_faq))
    # NTU_MB_Bot_Dispatcher.add_handler(cancel_handler)
    # echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    # NTU_MB_Bot_Dispatcher.add_handler(echo_handler)
    NTU_MB_Bot_Dispatcher.add_handler(CallbackQueryHandler(button))
    NTU_MB_Bot_Dispatcher.add_handler(CallbackQueryHandler(adminbutton))
    # NTU_MB_Bot_Dispatcher.add_handler(conv_handler)
    NTU_MB_Bot_Dispatcher.add_handler(CommandHandler('BoxA', command_TelegramboxA))
    NTU_MB_Bot_Dispatcher.add_handler(CommandHandler('BoxB', command_TelegramboxB))
    NTU_MB_Bot_Dispatcher.add_handler(CommandHandler('console', admin))
    NTU_MB_Bot_Dispatcher.add_handler(ShippingQueryHandler(command_Telgrambox_shippingquery))
    NTU_MB_Bot_Dispatcher.add_handler((PreCheckoutQueryHandler(command_Telgrambox_precheckoutquery)))
    NTU_MB_Bot_Dispatcher.add_handler(MessageHandler(Filters.successful_payment, command_Telgrambox_successfulpayment))

    # Inititates the bot! To stop the bot, write NTU_MB_Bot_Updater.stop() into the command console prompt.
    NTU_MB_Bot_Updater.start_polling()

    NTU_MB_Bot_Updater.idle()


if __name__ == '__main__':
    main()
