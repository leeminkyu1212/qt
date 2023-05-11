from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from test import Ui_MainWindow
import cv2
from time import *

transmode = 1


class MyThread(QThread):
    mySignal = Signal(QPixmap, QPixmap)

    def __init__(self):
        super().__init__()
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 480)
        self.cam.set(4, 320)

    def run(self):
        global transmode

        while True:
            ret, self.img = self.cam.read()
            if ret:
                if transmode == 1:
                    self.printImage1(self.img)
                elif transmode == 2:
                    self.printImage2(self.img)
                elif transmode == 3:
                    self.printImage3(self.img)
            sleep(0.1)

    def printImage1(self, imgBGR):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888)
        pix_img = QPixmap(img)

        imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
        imgCanny = cv2.Canny(imgGray, 100, 100)
        img2 = QImage(imgCanny, w, h, imgCanny.strides[0], QImage.Format_Grayscale8)
        pix_img2 = QPixmap(img2)

        self.mySignal.emit(pix_img, pix_img2)

    def printImage2(self, imgBGR):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888)
        pix_img = QPixmap(img)

        imgBlur = cv2.blur(imgBGR, (10, 10))
        img2 = QImage(imgBlur, w, h, byte * w, QImage.Format_Grayscale8)
        pix_img2 = QPixmap(img2)

        self.mySignal.emit(pix_img, pix_img2)

    def printImage3(self, imgBGR):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888)
        pix_img = QPixmap(img)

        imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
        imgBinarized = cv2.adaptiveThreshold(imgGray,
                                             255,
                                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY,
                                             99,
                                             10)
        img2 = QImage(imgBinarized, w, h, imgBinarized.strides[0], QImage.Format_Grayscale8)
        pix_img2 = QPixmap(img2)

        self.mySignal.emit(pix_img, pix_img2)


class myapp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.th = MyThread()
        self.th.mySignal.connect(self.setImage)

    def setImage(self, img, img2):
        self.pic1.setPixmap(img)
        self.pic2.setPixmap(img2)

    def mode(self):
        global transmode
        transmode += 1
        if transmode > 3:
            transmode = 1

    def play(self, img):
        self.th.start()

    def closeEvent(self, event):
        self.th.terminate()
        self.th.wait(3000)
        self.close()


app = QApplication()
win = myapp()
win.show()
app.exec_()
