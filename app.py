from abc import ABC, abstractmethod
from presentation.screen import Screen


class Context(ABC):
    def __init__(self, connection, http_requests):
        self.connection = connection
        self.httpRequests = http_requests


class App(ABC, Context):

    def __init__(self, connection, http_request):
        super().__init__(connection, http_request)

    @abstractmethod
    def on_connected(self):
        pass

    @abstractmethod
    def on_disconnected(self):
        pass

    @abstractmethod
    def build_screen(self, parent: Screen) -> Screen:
        pass

    @abstractmethod
    def on_connection_problem(self, msg):
        pass
