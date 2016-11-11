import sys

from PyQt5 import QtWidgets

from ui_test import Ui_Form
from PyQt5.QtWidgets import QInputDialog,QLineEdit

class Newwindow(QtWidgets.QWidget,Ui_Form):

    def __init__(self):
        super(Newwindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.msg)

    def msg (self):
        doublenum,ok1=QInputDialog.getDouble(self,"","",37.56,-1000,1000,2)
        print (doublenum,ok1)
        stringnum,ok3=QInputDialog.getText(self,"标题","姓名",QLineEdit.Normal,"王尼玛")
        print(stringnum,ok3)
        items=['春','夏','秋','冬']
        item,ok4=QInputDialog.getItem(self,"标题","season",items,1,True)
        print (item,ok4)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Newwindow()
    w.show()
    sys.exit(app.exec_())
