from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from ui.ui_main_qgraphics_view import Ui_MainWindow
import sys
import math
import random

from PyQt5.QtCore import (QEasingCurve, QFileInfo, QLineF, QMimeData,
        QParallelAnimationGroup, QPoint, QPointF, QPropertyAnimation, qrand,
        QRectF, qsrand, Qt, QTime)
from PyQt5.QtGui import (QBrush, QColor, QDrag, QImage, QPainter, QPen,
        QPixmap, QTransform)
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsObject,
        QGraphicsScene, QGraphicsView)

class node(QtWidgets.QGraphicsItem):
    def __init__(self):
        super(node,self).__init__()
        self.color = QColor(qrand() % 256, qrand() % 256, qrand() % 256)
        self.timer = QtCore.QBasicTimer()



    def boundingRect(self):
        return QtCore.QRectF(-15.5, -15.5, 34, 34)

    def paint(self,painter,option,widget):
        painter.save()#保存状态
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGray)
        painter.drawEllipse(-12, -12, 30, 30)
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(self.color))
        painter.drawEllipse(-15, -15, 30, 30)
        painter.restore()#恢复状态，需要成对使用


    def mousePressEvent(self, event):
        self.setCursor(Qt.ClosedHandCursor)#在经过对象时，鼠标左键按下时的光标设置

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)  #在经过对象时，鼠标松开时的光标设置



class myobj(QGraphicsObject):
    def __init__(self, parent=None):
        super(myobj, self).__init__(parent)

        self.color = QColor(Qt.lightGray)
        animation = QParallelAnimationGroup(self)

        rot_animation = QPropertyAnimation(self, b'rotation')
        rot_animation.setStartValue(-200)
        rot_animation.setEndValue(600)
        rot_animation.setEasingCurve(QEasingCurve.SineCurve)
        rot_animation.setDuration(3000)
        animation.addAnimation(rot_animation)

        animation.setLoopCount(-1)
        animation.start()

    def boundingRect(self):
        return QtCore.QRectF(-32.5, -32.5, 40, 40)

    def paint(self,painter,option,widget):
        painter.save()#保存状态

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(random.randint(100,200),random.randint(100,200),random.randint(100,200),random.randint(70,255))))
        painter.drawEllipse(-5, -5, 5, 5)

        painter.restore()#恢复状态，需要成对使用



class Newwindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Newwindow,self).__init__()
        self.setupUi(self)
        self.myscene=QtWidgets.QGraphicsScene()
        self.myscene.setSceneRect(0.0,0.0,0.0,0.0)
        self.myscene.setBackgroundBrush(QtGui.QColor(100, 100, 100, 255))
        self.setWindowTitle('QGraphicsView test')
        self.graphicsView.setScene(self.myscene)


        # brush=QtGui.QBrush(QtGui.QColor(255, 0, 0, 20))
        # pen=QtGui.QPen(QtGui.QColor(255, 100, 0, 127))
        # self.myscene.addEllipse(0, 0, 300, 60,pen,brush)
        # self.myscene.addEllipse(0, 100, 300, 60,pen,brush)
        # self.myscene.addText("彩云", QtGui.QFont("华文彩云", 120))
        for i in range(500):
            item = myobj()
            item.setPos(random.randint(10,600),random.randint(10,400))
            self.myscene.addItem(item)

        for i in range(10):
            item = node()
            item.setPos(random.randint(10,600),random.randint(10,400))
            self.myscene.addItem(item)

        self.myscene.addItem(myobj())

    def mouseDoubleClickEvent(self, *args, **kwargs):
        pass

    def mouseMoveEvent(self, *args, **kwargs):
        pass

    def mousePressEvent(self, *args, **kwargs):
        pass

    def mouseReleaseEvent(self, *args, **kwargs):
        pass

    def moveEvent(self, *args, **kwargs):
        pass

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Newwindow()
    w.show()
    sys.exit(app.exec_())