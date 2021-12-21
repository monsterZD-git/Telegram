# https://python-scripts.com/install-flask-green-unicorn-on-ubuntu
# https://habr.com/ru/post/552052/

from flask import Flask, request
import telebot

bot = telebot.TeleBot('KEY')
bot.set_webhook(url="URL")
app = Flask(__name__)

@app.route('/', methods=["POST"])
def webhook():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
    )
    return "ok"

@bot.message_handler(func=lambda message: True)
def echo_all(message):  
    bot.reply_to(message, 'asdfasdf')
	
if __name__ == "__main__":
    app.run()
