from app import App
from presentation.screen import Screen
from engine.run import run_app
from connection import SocketConnection


class MyApp(App):

    def on_connected(self):
        pass

    def on_disconnected(self):
        pass

    def build_screen(self, parent: Screen) -> Screen:
        pass

    def on_connection_problem(self, msg):
        pass


run_app(MyApp, SocketConnection(), "192.168.9.6", "8080", "raspberryPI", "normal device")
