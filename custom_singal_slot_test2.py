from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class SinClass(QtCore.QObject):
    sin1 =QtCore.pyqtSignal(list)
    sin2 = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super(SinClass, self).__init__(parent)
        self.sin1.connect(self.sin1Call)
        self.sin2.connect(self.sin2Call)

        self.sin1.emit([1,2,3,4])
        self.sin2.emit({1:'1',2:'2'})

    def sin1Call(self,val):
        print("sin1 emit:",val)

    def sin2Call(self, val):
        print("sin2 emit:",val)


sin=SinClass()