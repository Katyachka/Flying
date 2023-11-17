from telebot.async_telebot import AsyncTeleBot

from django.conf import settings

bot = AsyncTeleBot(settings.BOT_TOKEN, parse_mode='Markdown')


@bot.message_handler(commands = ['start', 'help'])
async def send_welcome(message):
    await bot.send_message(message.chat.id, f'{message.chat.first_name}, вітаємо Вас у Flying бот. Цей бот допоможе Вам придбати авіаквитки✈️')


@bot.message_handler(func = lambda message: True)
async def error_message(message):
    await bot.reply_to(message, f"Вибачте, '*{message.text}*' команда не підтримується👉👈")