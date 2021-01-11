from abc import ABC, abstractmethod


class BaseScreen(ABC):

    @abstractmethod
    def add_controller_group(self, layout):
        pass

    @abstractmethod
    def _build(self):
        pass


class Screen(BaseScreen):
    def __init__(self):
        self.parent = []

    def add_controller_group(self, layout):
        pass

    def _build(self):
        pass
