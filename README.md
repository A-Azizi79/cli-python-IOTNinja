# IOTNinja

IOTNinja is a Python library for dealing with word pluralization.

![alt text](http://www.upsara.com/images/x581442_.png)

</br>
</br>
</br>


![alt text](http://www.upsara.com/images/n942896_.jpg)

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


## Documentation 🇬🇧


<div dir="rtl">

## مفاهیم 

  < - Controller کنترلر ها المنت هایی هستند که ما داخل صفحه موبایلمون یا وبمون میبینیم و میتونیم با اون تعامل داشته باشیم برای مثال دکمه ها و یا متن ها یا مثلا عکس ها و ...

  < - ControllerGroup کنترلرگروپ ها گروهی از کنترلر (Controller) ها هستند که میتونن در کنار هم قرار بگیرن (HorizontalControllerGroup به صورت افقی)  و یا در زیر هم قرار بگیرند (VerticalControllerGroup به صورت عمودی ) مثل عکس زیر

![alt text](https://www.tutlane.com/images/android/android_linearlayout_example_diagram.png)

## توضیحات


شما میتوانید با استفاده از IOTNinja دستگاه های خود (RaspberryPi, arduino, etc..) را از راه دور توسط موبایل و یا از طریق وب کنترل کنید (در حال حاظر این امکان فقط برای موبایل های اندرویدی وجود دارد منتظر بروزرسانی های ما باشید) اما نکته جالب اینجاست که شما میتوانید قابلیت های دستگاه خود را در دیوایس خودتون (چون اینجا ریپوزیتوری کتابخونمون با زبان پایتونه ما دستگاه رو رزبری پای در نظر میگیریم) تعریف کنید برای مثال شما میتونید در داخل کد پایتونتون تعریف کنید که ما یک دکمه باید در دیوایس اندروید داشته باشیم که هروقت روی آن کلیک شد این تابع اجرا شود (مثلا تابعی که باعث میشه چراغ های خونه روشن شه!)  راحته مگه نه ؟ 🤪

خب خب همه ی این جذابیت ها توی تابع build_screen رخ میده این تابع یک پارامتر داره به اسم parent  که این پارامتر همون صفحه اصلی ما تو موبایلمون و یا توی وبه این پارامتر ما که یه آبجکت از کلاس Screen  هست یک متد داره به اسم add_controller_group که این تابع میاد گروهی از کنترلر هامون رو به صفحه وبمون یا موبایلمون اضافه میکنه 
 
## مستندات 🇮🇷 

</div>


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
