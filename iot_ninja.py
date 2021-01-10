from abc import ABC, abstractmethod
from socketio import client as Socket
import paho.mqtt.client as mqtt
import json
import enum
import key_constants as constant


class ConnectionMode(enum.Enum):
    socket = 1001
    mqtt = 1002


class Context(ABC):
    def __init__(self, connection):
        self.connection = connection


class IOTNinja(ABC):

    def __init__(self, device_name, description, server, port, connection, scaffold):
        self.identity = {
            "deviceName": device_name,
            "description": description,
            "scaffold": scaffold.parentController
        }
        self.deviceName = device_name
        self.deviceName = description
        self.server = server
        self.port = port
        self.scaffold = scaffold
        global_connection = connection


class Connection(ABC):
    @abstractmethod
    def connection_type(self, ):
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


class MqttConnection(Connection):

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


class SocketConnection(Connection):

    def __init__(self, address):
        self.socket = Socket.Client()
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


class Run:
    def __init__(self, app):
        if isinstance(app, IOTNinja):
            global_connection.connect(app.server + ":" + str(app.port))
            global_connection.emit(constant.IDENTITY, app.identity)
        else:
            raise Exception("you need to pass app !")


global_connection = SocketConnection("")
