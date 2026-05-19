import telebot
from googletrans import Translator

BOT_TOKEN = "8826567637:AAG-6-o-a0svdIvfDMZdg64kWhF2iH3f03A"

bot = telebot.TeleBot(BOT_TOKEN)
translator = Translator()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Tarjimon botga xush kelibsiz!\n/uz /ru /en")

@bot.message_handler(func=lambda m: True)
def auto_translate(message):
    detected = translator.detect(message.text)
    if detected.lang == 'uz':
        result = translator.translate(message.text, dest='ru')
        bot.reply_to(message, f"🇷🇺 {result.text}")
    else:
        result = translator.translate(message.text, dest='uz')
        bot.reply_to(message, f"🇺🇿 {result.text}")

bot.infinity_polling()
