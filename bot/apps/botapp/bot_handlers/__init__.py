from bot.apps.botapp.bot_handlers.handler_chain import HandlerChain
from bot.apps.botapp.bot_handlers.personal_data_menu_handler import PersonalDataMenuHandler

HANDLER_CHAIN = HandlerChain()
HANDLER_CHAIN.add_handler(PersonalDataMenuHandler())
