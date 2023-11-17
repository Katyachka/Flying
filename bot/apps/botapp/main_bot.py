from telebot.async_telebot import AsyncTeleBot

from django.conf import settings

bot = AsyncTeleBot(settings.BOT_TOCKEN, parse_mode='Markdown')


@bot.message_handler(commands = ['start', 'help'])
async def send_welcome(message):
    await bot.reply_to(message, 'Вас вітає Flying бот, який допоможе вам придбати авіаквитки✈️')


@bot.message_handler(func = lambda message: True)
async def error_message(message):
    await bot.reply_to(message, f"Вибачте, {message.text} команда не підтримується👉👈")