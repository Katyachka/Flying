from abc import abstractmethod, ABC


class Handler(ABC):

    @abstractmethod
    def can_handle(self, message) -> bool:
        pass

    @abstractmethod
    async def handle(self, message, bot) -> None:
        pass


class HandlerChain:

    def __init__(self):
        self.handlers: list = []

    def add_handler(self, handler: Handler):
        self.handlers.append(handler)

    async def handle_message(self, message, bot):
        for handler in self.handlers:
            if handler.can_handle(message):
                await handler.handle(message, bot)
                break
