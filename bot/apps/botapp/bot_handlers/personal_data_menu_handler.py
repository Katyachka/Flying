
from telebot import types

from bot.apps.botapp.bot_callbacks.personal_data_menu_callback_handler import SEE_DATA, EDIT_DATA
from bot.apps.botapp.bot_handlers.handler_chain import Handler


class PersonalDataMenuHandler(Handler):

    def __init__(self):
        self.COMMAND = "personal_data_menu"

    def can_handle(self, message) -> bool:
        return message.text == f'/{self.COMMAND}'

    async def handle(self, message, bot) -> None:
        await bot.send_message(message.chat.id, f'Оберіть дію:', reply_markup=reply_markup)


reply_markup = types.InlineKeyboardMarkup()
see_data = types.InlineKeyboardButton('Передивитись особисті дані', callback_data=SEE_DATA)
edit_data = types.InlineKeyboardButton('Редагувати особисті дані', callback_data=EDIT_DATA)
reply_markup.row(see_data, edit_data)
