from iot_ninja import globalConnection
import requests

import key_constants

class UiController:
    def __init__(self):
        self.parentController = {}
    
    def addControllerLayout(self, layout):
        pass


class Controller(ABC):
    def __init__(self, id):
        self.controller = {constant.ID: id}

    def _get(self):
        return self.controller

    def _defineType(self, type):
        self.controller[constant.TYPE] = type

class ControllerGroup(ABC):
    def __init__(self, id):
        self.controllerGroup = {constant.ID: id, constant.CHILDS: []}

    def _get(self):
        return self.controllerGroup

    def add(self, controller):
        if(isinstance(controller, Controller)):
            self.controllerGroup[CHILDS].append(controller)
        else : raise Exception("your controller need to be instance of Controller")    
        
        
class VerticalGroupController(ControllerGroup):
    def __init__(self, id):
        super.__init__(id)
        self.controllerGroup[constant.TYPE] = "VerticalGroupController"

class HorizontalGroupController(ControllerGroup):
    def __init__(self, id):
        super.__init__(id)
        self.controllerGroup[constant.TYPE] = "HorizontalGroupController"


class StackGroupController(ControllerGroup):
    pass

class TextController(Controller):
    def __init__(self, id, text, size = 12, color = "#000000"):
        self.__init__(id)
        self._defineType("text")
        self.controller["text"] = text
        self.controller["size"] = size
        self.controller["color"] = color

class InputController(Controller):
    def __init__(self, id):
        self.__init__(id)
        self._defineType("input")

    def getValue(self, callback):
        globalConnection.emit(constant.GET_VALUE, callback)


class ButtonController(Controller):
    def __init__(self, id, onClickListener):
        self.__init__(id)
        self._defineType("button")
        globalConnection.defineEvent("btn_"+str(id), onClickListener)


class ImageController(Controller):
    def __init__(self, id):
        self.__init__(id)
        self._defineType("image")
    
    def setImage(self, path):
        files = {'media': open(path, 'rb')}
        requests.post(constant.SERVER_ADDRESS, files=files)
        