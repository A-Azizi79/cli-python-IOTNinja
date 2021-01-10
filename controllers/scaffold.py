from abc import ABC, abstractmethod
from base_controllers import ControllerGroup
from iot_ninja import Context
import exceptions
import json


class Scaffold(ABC, Context):
    def __init__(self, connection):
        super().__init__(connection)
        self.__parentController = []

    @abstractmethod
    def add_controller_group(self, layout):
        pass

    @abstractmethod
    def _build(self):
        pass


class IOTNinjaApp(Scaffold):
    def __init__(self, connection):
        super().__init__(connection)

    def add_controller_group(self, controller_group):
        if exceptions.is_valid_param(ControllerGroup, controller_group):
            self.parentController.append(controller_group)

    def _build(self):
        return json.dumps(self.parentController)
