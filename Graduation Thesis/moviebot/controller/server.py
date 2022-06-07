"""This file contains the flask server."""

from moviebot.controller.controller_telegram import ControllerTelegram
from flask import Flask, request
from os import environ
import yaml
import telegram

app = Flask(__name__)
controller_telegram = ControllerTelegram()
telegram_token = '5395029377:AAFM_bk9V73WHRE0VJPOpnjrleZ4XWQIxco'
bot = telegram.Bot(token=telegram_token)

@app.route('/{}'.format(telegram_token), methods=['POST'])
def respond():
    """Receives to Telegram POST request"""
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    text = update.message.text.encode('utf-8').decode()

    if text == "/start":
        controller_telegram.start(update, True)
    elif text == "/restart":
        controller_telegram.start(update, True)
    elif text == "/help":
        controller_telegram.help(update, True)
    elif text == "/exit":
        controller_telegram.exit(update, True)
    else:
        controller_telegram.continue_conv(update, True)
    return 'ok'


