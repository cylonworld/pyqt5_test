import sys

from PyQt5 import QtWidgets

from ui.ui_test import Ui_Form


class Newwindow(QtWidgets.QWidget,Ui_Form):

    def __init__(self):
        super(Newwindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.msg)

    def msg (self):
        QtWidgets.QMessageBox.information(self,"标题","消息",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Newwindow()
    w.show()
    sys.exit(app.exec_())