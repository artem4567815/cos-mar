from pyPS4Controller.controller import Controller
from main2 import spawn_bullet

class MyControoler(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    def on_x_press(self):
        spawn_bullet()
    def on_x_release(self):
        print("Goodbye")


controller = MyControoler(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(timeout=60)
controller.on_x_press()
controller.on_x_release()
