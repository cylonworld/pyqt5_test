from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import random
text=["文本改变","文本不改变","文本还是改变吧"]

def sinText():
    btn1.setText(random.choice(text))


app=QtWidgets.QApplication([])

main=QtWidgets.QWidget()
main.resize(200,100)
btn1=QtWidgets.QPushButton("按钮文本",main)
btn1.resize(200,30)
btn1.clicked.connect(sinText)



main.show()

app.exec_()