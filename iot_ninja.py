from abc import ABC, abstractmethod
from socketio import client as Socket
import paho.mqtt.client as mqtt
import json
import enum


class ConnectionMode(enum.Enum):
    socket = 1001
    mqtt = 1002


class IOTNinja(ABC):

    def __init__(self, device_name, description, server, port, connection_mode, ui_controller):
        self.deviceName = device_name
        self.deviceName = description
        self.server = server
        self.port = port
        self.connection_mode = connection_mode
        self.ui_controller = ui_controller

    def change_connection_mode_to(self, connection_mode):
        self.connection_mode = connection_mode

    @abstractmethod
    def on_connection_open(self):
        pass

    @abstractmethod
    def on_disconnected(self):
        pass


class Connection(ABC):
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
    def emit(self, name, ack):
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

    def emit(self, name, ack):
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

    def emit(self, name, ack):
        self.socket.emit(name, callback=ack)


globalConnection = SocketConnection("")
