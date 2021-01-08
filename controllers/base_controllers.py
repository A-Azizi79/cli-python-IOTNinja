import key_constants as constant
from abc import ABC, abstractmethod


class Scaffold(ABC):
    def __init__(self):
        self.parentController = {}

    @abstractmethod
    def add_controller_group(self, layout):
        pass

    @abstractmethod
    def build(self):
        pass


class Controller(ABC):
    def __init__(self, c_id):
        self.controller = {constant.ID: c_id}

    def _get(self):
        return self.controller

    def _define_type(self, controller_type):
        self.controller[constant.TYPE] = controller_type


class ControllerGroup(ABC):
    def __init__(self, cg_id):
        self.controllerGroup = {constant.ID: cg_id, constant.CHILDS: []}

    def _get(self):
        return self.controllerGroup

    def add(self, controller):
        if isinstance(controller, Controller):
            self.controllerGroup[constant.CHILDS].append(controller)
        else:
            raise Exception("your controller need to be instance of Controller")
