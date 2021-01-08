from abc import ABC
from socketio import client as Socket
import paho.mqtt.client as mqtt
import json

class ConnectionMode(enum.Enum):
    socket = 1001
    mqtt = 1002

class IOTNinja(ABC) :
    def __init__(self, deviceName, description, server, port):
        self.deviceName = deviceName
        self.deviceName = description
        self.server = server
        self.port = port
    
    def setConnectionMode(connectionMode):
        self.connectionMode = connectionMode
    
      
    @abstractmethod
    def onConnectionOpen():
        pass

    @abstractmethod
    def onDisconnected():
        pass


class Connection(ABC) :
    @abstractmethod
    def connect(self, server):
        pass

    @abstractmethod
    def disconnect(self, server):
        pass
    
    @abstractmethod
    def defineEvent(self, eventName, callBack) :
        pass

    @abstractmethod
    def listener(self, callback):
        pass

    @abstractmethod
    def freezConnection(self):
        pass
    
    @abstractmethod
    def emit(self, name, ack):
        pass

class MqttConnection(Connection):
    def connect(server):
        pass

    def disconnect(server):
        pass
    
    def action():
        pass

    def listener(callback):
        pass

    def freezConnection():
        pass

class SocketConnection(Connection):

    def __init__(self, address):
        self.socket = Socket.Client()
        self.socket.connect(address)

    def connect(self, server, address):
        if(self.socket.connected):
            print("already connected!")
        else :
            self.socket.connect()
                
    def disconnect(self, server):
        if(self.socket.connected):
            self.socket.disconnect
        else:
            print("there is no connection!")
    
    def defineEvent(self, eventName, callback):
        self.socket.on(eventName, callback)

    def listener(self, callback):
        pass

    def freezConnection(self):
        pass
    
    def emit(self, name, ack):
        self.socket.emit(name, callback= ack)

globalConnection = SocketConnection()
    