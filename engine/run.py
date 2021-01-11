from ..connection import Connection, HttpRequestsImpl
from ..app import App
import key_constants as constant


def run_app(ref_app, connection: Connection, server_address, server_port, device_name, device_description) -> None:
    final_address = server_address + ":" + str(server_port)
    try:
        app = ref_app()
        if isinstance(app, App):
            app.connection = connection
            app.http_request = HttpRequestsImpl(final_address)
            app.connection.connect(final_address)
            if app.connection.connected():
                app.on_connected()
                app.connection.emit(constant.IDENTITY, {
                    constant.DEVICE_NAME: device_name,
                    constant.DEVICE_DESCRIPTION: device_description
                })

                connection.freeze_connection()
            else:
                app.on_connection_problem("")
    except Exception as err:
        print("we got a problem! -> ", err)
