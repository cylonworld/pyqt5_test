import sys

from PyQt5 import QtWidgets
from ui.ui_main import Ui_MainWindow

from ui.ui_child import Ui_Form


class Newwindow(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(Newwindow,self).__init__()
        self.setupUi(self)
        self.child=ChildrenForm()
        self.fileopen.triggered.connect(self.msg)
        self.actionShow.triggered.connect(self.childShow)
        self.actionClose.triggered.connect(self.childClose)



    def msg (self):
        file, ok = QtWidgets.QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);Text Files (*.txt)")
        self.statusbar.showMessage(file)

    def childShow(self):
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def childClose(self):
        self.child.close()

class ChildrenForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(ChildrenForm,self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Newwindow()
    w.show()
    sys.exit(app.exec_())