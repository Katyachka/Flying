from bot.apps.botapp.bot_handlers.handler_chain import HandlerChain
from bot.apps.botapp.bot_handlers.main_menu_hanlder import MainMenuHandler

HANDLER_CHAIN = HandlerChain()
HANDLER_CHAIN.add_handler(MainMenuHandler())
