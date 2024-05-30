import telebot
from threading import Thread
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import subprocess

# Замените значения YOUR_BOT_TOKEN на ваш токен бота
import telebot
from threading import Thread
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import subprocess

# Замените значения YOUR_BOT_TOKEN на ваш токен бота
bot_token = '6758909655:AAFuHmzMBqrc7_B6OiuwidkAcfgGqeSkp3o'
bot = telebot.TeleBot(bot_token)

# Укажите ваш локальный IP-адрес
local_ip = 'https://jenyahard.github.io/telegram_web_app/'

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Нажмите кнопку /webapp чтобы перейти в веб приложение.")

# Обработчик команды /webapp
@bot.message_handler(commands=['webapp'])
def send_webapp_link(message):
    markup = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton(
        text="Открыть WebApp",
        web_app=WebAppInfo(url=local_ip)
    )
    markup.add(web_app_button)
    bot.send_message(message.chat.id, "Нажмите кнопку ниже, чтобы открыть WebApp.", reply_markup=markup)

def run_bot():
    bot.polling()

if __name__ == '__main__':
    # Запуск Flet веб-приложения в отдельном потоке
    flet_thread = Thread(target=lambda: subprocess.run(["python", "webapp.py"]))
    flet_thread.setDaemon(True)
    flet_thread.start()

    # Запуск бота
    run_bot()
