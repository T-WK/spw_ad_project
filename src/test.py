import sys
import urllib.request
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Qpixmap_App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lb_img = QLabel()


        self.lb_img.setPixmap(QPixmap("TextRPG_pack/Art/모험가.jpeg"))
        vbox = QVBoxLayout()
        vbox.addWidget(self.lb_img)
        self.setLayout(vbox)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ax = Qpixmap_App()
    sys.exit(app.exec_())