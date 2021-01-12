from abc import ABC, abstractmethod
from presentation.base_controllers import ControllerGroup


class BaseScreen(ABC):

    @abstractmethod
    def add_controller_group(self, layout):
        pass

    @abstractmethod
    def _build(self):
        pass


class Screen(BaseScreen):
    def __init__(self):
        self.__children = []

    def add_controller_group(self, group: ControllerGroup):
        self.__children.append(group)

    def _build(self):
        pass