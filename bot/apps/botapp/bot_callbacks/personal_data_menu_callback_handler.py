from bot.apps.botapp.bot_callbacks.callback_chain import CallbackHandler

SEE_DATA = "see_data"
EDIT_DATA = "edit_data"


class PersonalDataMenuCallbackHandler(CallbackHandler):

    def can_handle(self, callback) -> bool:
        return callback.data == SEE_DATA or callback.data == EDIT_DATA

    async def handle(self, callback, bot) -> None:
        command = None
        if callback.data.startswith('see'):
            command = 'see'
        else:
            command = 'edit'
        await bot.send_message(callback.message.chat.id, f"I Handled {command}")
