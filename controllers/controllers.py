from base_controllers import Controller
from iot_ninja import globalConnection
import key_constants as constant
import requests


class TextController(Controller):
    def __init__(self, text, c_id, size=12, color="#000000"):
        super().__init__(c_id)
        self._define_type("text")
        self.controller[constant.TEXT] = text
        self.controller[constant.SIZE] = size
        self.controller[constant.COLOR] = color


class InputController(Controller):
    def __init__(self, c_id):
        super().__init__(c_id)
        self._define_type("input")

    # noinspection PyMethodMayBeStatic
    def get_value(self, callback):
        globalConnection.emit(constant.GET_VALUE, callback)


class ButtonController(Controller):
    def __init__(self, c_id, on_click_listener):
        super().__init__(c_id)
        self._define_type("button")
        globalConnection.defineEvent("btn_" + str(c_id), on_click_listener)


class ImageController(Controller):
    def __init__(self, c_id):
        super().__init__(c_id)
        self._define_type("image")

    # noinspection PyMethodMayBeStatic
    def set_image(self, path):
        files = {'media': open(path, 'rb')}
        requests.post(constant.SERVER_ADDRESS, files=files)


class ChartController(Controller):
    def __init__(self, c_id):
        super().__init__(c_id)

    def add_data(self, data):
        globalConnection.emit("chart_add_" + str(self.c_id), data)
