# IOTNinja

IOTNinja is a Python library for dealing with word pluralization.

![alt text](https://uupload.ir/files/vxha_new_project_(1).png)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install IOTNinja.

```bash
pip install iotninja
```

## Usage

```python
from app import App
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

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
