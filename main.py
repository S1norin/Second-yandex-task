import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui.ui", self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)
        color = QColor(255, 255, 0, 100)
        painter.setBrush(color)
        for i in range(20):
            coords = QPoint(randint(1, 300), randint(1, 300))
            radius = randint(1, 30)
            painter.drawEllipse(coords, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Circles()
    window.show()
    sys.exit(app.exec_())
