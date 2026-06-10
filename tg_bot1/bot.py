import telebot
from ai import get_answer
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(token)


@bot.message_handler(func=lambda message: True)
def chat(message):

    try:
        answer = get_answer(message.text)

        bot.send_message(
            message.chat.id,
            answer
        )

    except Exception as e:

        bot.send_message(
            message.chat.id,
            f"Ошибка: {e}"
        )

print("Бот запущен")
bot.infinity_polling()