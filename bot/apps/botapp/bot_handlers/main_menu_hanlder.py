from bot.apps.botapp.bot_handlers.handler_chain import Handler


class MainMenuHandler(Handler):

    def __init__(self):
        self.COMMAND = "personal_data"

    def can_handle(self, message) -> bool:
        return message.text == f'/{self.COMMAND}'

    async def handle(self, message, bot) -> None:
        await bot.send_message(message.chat.id, f'i handle it')

