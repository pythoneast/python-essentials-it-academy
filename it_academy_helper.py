import telebot
from datetime import datetime

bot = telebot.TeleBot("1608584366:AAGcY_L1W0YEcU5uH7Stf4bN3zcF_Dmekow")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, чем могу помочь?")


@bot.message_handler(commands=['weather'])
def get_temperature(message):
	bot.reply_to(message, "Температура: 28 градусов выше нуля!")


@bot.message_handler(commands=['time'])
def get_current_time(message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bot.reply_to(message, f"Время: {current_time}")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "Я тебя не понимаю :(")


if __name__ == "__main__":
    bot.polling()
