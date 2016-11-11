from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


global sec
sec=0

class WorkThread(QtCore.QThread):
    trigger=QtCore.pyqtSignal()

    def __init__(self):
        super(WorkThread,self).__init__()

    def run(self):
        for i in range(200000000):
            pass
        self.trigger.emit()


def countTime():
    global sec
    sec+=1
    lcdNumber.display(sec)

def work():
    timer.start(1000)
    workThread.start()
    workThread.trigger.connect(timeStop)

def timeStop():
    timer.stop()
    print ("运行结束",lcdNumber.value())
    global sec
    sec=0

app=QtWidgets.QApplication([])
top=QtWidgets.QWidget()
layout=QtWidgets.QVBoxLayout(top)
lcdNumber=QtWidgets.QLCDNumber()
layout.addWidget(lcdNumber)
button=QtWidgets.QPushButton("测试")
layout.addWidget(button)

timer=QtCore.QTimer()
workThread=WorkThread()

button.clicked.connect(work)
timer.timeout.connect(countTime)

top.show()
app.exec_()