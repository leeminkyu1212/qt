from PySide2.QtWidgets import *
from test import Ui_Form
from sense_hat import SenseHat
from time import sleep


class MyApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

        self.r=0
        self.g=0
        self.b=0

    def main(self):
        self.sense = SenseHat()

    def flash(self):
        for y in range(8):
            for x in range(8):
                self.sense.set_pixel(x,y,255,255,255)

    def clear(self):
        for y in range(8):
            for x in range(8):
                self.sense.set_pixel(x,y,0,0,0)

    def click(self, x, y):


        self.sense.set_pixel(x,y,self.r,self.g,self.b)

    def rslide(self, val):
        self.r=val

    def gslide(self, val):
        self.g=val

    def bslide(self, val):
        self.b=val


app = QApplication()
win = MyApp()
win.show()
app.exec_()
