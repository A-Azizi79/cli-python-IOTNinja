import key_constants as constant
from abc import ABC, abstractmethod
import exceptions


class ControllerCore(ABC):
    @abstractmethod
    def _build(self):
        pass

    @abstractmethod
    def define_type(self, controller_type):
        pass


class Controller(ABC, ControllerCore):
    def __init__(self, c_id):
        self.c_id = c_id
        self.controller = {constant.ID: c_id}

    def _build(self):
        return self.controller

    def _define_type(self, controller_type):
        self.controller[constant.TYPE] = controller_type


class DynamicController(ABC, Controller):
    def __init__(self, c_id, context):
        super().__init__(c_id)
        self.context = context


class ControllerGroup(ABC, ControllerCore):
    def __init__(self, cg_id):
        self.controllerGroup = {constant.ID: cg_id, constant.CHILDREN: []}

    def _build(self):
        return self.controller

    def add(self, controller):
        if exceptions.is_valid_param(Controller, controller):
            self.controllerGroup[constant.CHILDREN].append(controller)

    def _define_type(self, controller_type):
        self.controllerGroup[constant.TYPE] = controller_type
