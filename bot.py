# Замените значения YOUR_BOT_TOKEN на ваш токен бота
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery



# Замените значения YOUR_BOT_TOKEN на ваш токен бота
bot_token = '6758909655:AAFuHmzMBqrc7_B6OiuwidkAcfgGqeSkp3o'
bot = telebot.TeleBot(bot_token)

# Укажите ваш локальный IP-адрес
local_ip = 'https://jenyahard.github.io/telegram_web_app/'

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton(
        text="Открыть WebApp",
        web_app=WebAppInfo(url=local_ip)
    )
    markup.add(web_app_button)
    bot.send_message(message.chat.id, "Нажмите кнопку ниже, чтобы открыть WebApp.", reply_markup=markup)

# Обработчик callback_query
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call: CallbackQuery):
    data = call.data  # данные, полученные из веб-приложения
    bot.send_message(call.message.chat.id, f"Получены данные из WebApp: {data}")


def run_bot():
    bot.polling()


if __name__ == '__main__':
    # Запуск бота
    run_bot()
