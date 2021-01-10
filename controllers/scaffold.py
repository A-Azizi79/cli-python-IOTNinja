from abc import ABC, abstractmethod
from base_controllers import ControllerGroup
import exceptions
import json


class Scaffold(ABC):
    def __init__(self):
        self.parentController = []

    @abstractmethod
    def add_controller_group(self, layout):
        pass

    @abstractmethod
    def _build(self):
        pass


class AppScaffold(Scaffold):
    def __init__(self):
        super().__init__()

    def add_controller_group(self, controller_group):
        if exceptions.is_valid_param(ControllerGroup, controller_group):
            self.parentController.append(controller_group)

    def _build(self):
        return json.dumps(self.parentController)
