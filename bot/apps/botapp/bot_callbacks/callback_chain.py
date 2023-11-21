from abc import abstractmethod, ABC


class CallbackHandler(ABC):

    @abstractmethod
    def can_handle(self, callback) -> bool:
        pass

    @abstractmethod
    async def handle(self, callback, bot) -> None:
        pass


class CallbackHandlerChain:

    def __init__(self):
        self.callbacks_handlers: list = []

    def add_callback_handler(self, callback_handler: CallbackHandler):
        self.callbacks_handlers.append(callback_handler)

    async def handle_callback(self, callback, bot):
        for callback_handler in self.callbacks_handlers:
            if callback_handler.can_handle(callback):
                await callback_handler.handle(callback, bot)
                break
