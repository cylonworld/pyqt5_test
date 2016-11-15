from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from ui.ui_main_qgraphics_view import Ui_MainWindow
import sys
import random

class Newwindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Newwindow,self).__init__()
        self.setupUi(self)
        self.myscene=QtWidgets.QGraphicsScene()
        self.myscene.setSceneRect(0.0,0.0,0.0,0.0)
        self.myscene.addLine(0, 0, 400, 400)
        self.setWindowTitle('QGraphicsView test')
        self.graphicsView.setScene(self.myscene)

    def mouseDoubleClickEvent(self, *args, **kwargs):
        pass

    def mouseMoveEvent(self, *args, **kwargs):
        pass

    def mousePressEvent(self, *args, **kwargs):
        print ("mouse pressed")
        self.myscene.addLine(0, 0, random.randint(100,700), random.randint(100,700))
        pass

    def mouseReleaseEvent(self, *args, **kwargs):
        pass

    def moveEvent(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Newwindow()
    w.show()
    sys.exit(app.exec_())