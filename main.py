from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint

class Krug(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setPen(QColor('yellow'))
            self.qp.setBrush(QColor('yellow'))
            self.zapros()
            self.qp.end()
            self.flag = False
    def zapros(self):
        for i in range(randint(10, 100)):
            a = randint(10, 100)
            self.qp.drawEllipse(randint(0, 400), randint(0, 300), a, a)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Krug()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())