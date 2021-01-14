from abc import ABC, abstractmethod
from presentation.screen import Screen


class Context(ABC):

    def __init__(self):
        self._connection = None
        self._http_request = None

    @property
    def http_request(self):
        return self._http_request

    @http_request.setter
    def http_request(self, new_obj):
        self._http_request = new_obj

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, new_obj):
        self._connection = new_obj


class App(Context):

    @abstractmethod
    def build_screen(self, parent: Screen) -> Screen:
        pass

    @abstractmethod
    def on_connected(self):
        pass

    @abstractmethod
    def on_disconnected(self):
        pass

    @abstractmethod
    def on_connection_problem(self, message):
        pass


class Cont(ABC):
    @abstractmethod
    def msg(self):
        pass


class TS(Cont):
    pass
