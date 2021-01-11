from abc import ABC, abstractmethod
import requests
from socketio import client as socket


class HttpRequests(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get(self, url, params=None, **kwargs):
        pass

    @abstractmethod
    def post(self, url, data=None, json=None, **kwargs):
        return requests.post(url, data)


class HttpRequestsImpl(HttpRequests):

    def get(self, url, params=None, **kwargs):
        pass

    def post(self, url, data=None, json=None, **kwargs):
        pass


class Connection(ABC):

    @abstractmethod
    def connection_type(self):
        pass

    @abstractmethod
    def connect(self, server):
        pass

    @abstractmethod
    def disconnect(self, server):
        pass

    @abstractmethod
    def define_event(self, event_name, callback):
        pass

    @abstractmethod
    def listener(self, callback):
        pass

    @abstractmethod
    def freeze_connection(self):
        pass

    @abstractmethod
    def emit(self, name, data, ack):
        pass

    @abstractmethod
    def connected(self):
        pass


class MqttConnection(Connection):

    def connection_type(self):
        pass

    def connect(self, server):
        pass

    def disconnect(self, server):
        pass

    def define_event(self, event_name, callback):
        pass

    def listener(self, callback):
        pass

    def freeze_connection(self):
        pass

    def emit(self, name, data, ack):
        pass

    def connected(self):
        pass


class SocketConnection(Connection):

    def __init__(self, address):
        self.socket = socket.Client()
        self.socket.connect(address)

    def connect(self, server):
        if self.socket.connected:
            print("already connected!")
        else:
            self.socket.connect("")

    def disconnect(self, server):
        if self.socket.connected:
            self.socket.disconnect()
        else:
            print("there is no connection!")

    def define_event(self, event_name, callback):
        self.socket.on(event_name, callback)

    def listener(self, callback):
        pass

    def freeze_connection(self):
        pass

    def emit(self, name, data, ack):
        self.socket.emit(name, data, callback=ack)

    def connection_type(self):
        return "socket"

    def connected(self):
        return self.socket.connected
