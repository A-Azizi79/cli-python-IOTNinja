from base_controllers import Controller, DynamicController
import key_constants as constant
import requests


class TextController(Controller):
    def __init__(self, text, c_id, size=12, color="#000000"):
        super().__init__(c_id)
        self._define_type("text")
        self.controller[constant.TEXT] = text
        self.controller[constant.SIZE] = size
        self.controller[constant.COLOR] = color


class InputController(DynamicController):
    def __init__(self, c_id):
        super().__init__(c_id)
        self._define_type("input")

    def get_value(self, callback):
        self.context.connection.emit(constant.GET_VALUE, callback)


class ButtonController(DynamicController):
    def __init__(self, c_id, on_click_listener):
        super().__init__(c_id)
        self._define_type("button")
        self.context.connection.defineEvent("btn_" + str(c_id), on_click_listener)


class ImageController(DynamicController):
    def __init__(self, c_id):
        super().__init__(c_id)
        self._define_type("image")

    def set_image(self, path):
        files = {'media': open(path, 'rb')}

        self.context.httpRequests.post(constant.SERVER_ADDRESS, files)


class ChartController(DynamicController):
    def __init__(self, c_id):
        super().__init__(c_id)

    def add_data(self, data):
        self.context.connection.emit("chart_add_" + str(self.c_id), data)
