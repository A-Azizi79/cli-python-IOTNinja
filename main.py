from app import App
from engine.run import run_app
from connection import SocketConnection
from presentation.screen import Screen
from presentation.controller_group import VerticalControllerGroup
from presentation.controllers import *


class MyApp(App):

    def build_top_card(self) -> VerticalControllerGroup:
        param = VerticalControllerGroup("vertical")
        param.add(TextController("hello world", "id32"))
        return param

    def on_connected(self):
        pass

    def on_disconnected(self):
        pass

    def build_screen(self, parent: Screen) -> Screen:
        parent.add_controller_group(self.build_top_card())
        return parent

    def on_connection_problem(self, msg):
        pass


run_app(MyApp, SocketConnection(), "192.168.9.6", "8080", "raspberryPI", "normal device")
