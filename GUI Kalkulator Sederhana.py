# Kalkulator Sederhana
from PyQt5.QtWidgets import *

app = QApplication([])

window = QMainWindow()
window.setGeometry(300,100,500,300)
window.setWindowTitle("Kalkulator")

grid = QGridLayout()

ednum = QLineEdit(window)
ednum.setFixedHeight(50)
ednum.setEnabled(False)

def buat_tombol(label):
    qbtn = QPushButton(label, window)
    qbtn.setFixedHeight(100)
    return qbtn

def set0():
    ednum.setText(f"{ednum.text()}0")
def set1():
    ednum.setText(f"{ednum.text()}1")
def set2():
    ednum.setText(f"{ednum.text()}2")
def set3():
    ednum.setText(f"{ednum.text()}3")
def set4():
    ednum.setText(f"{ednum.text()}4")
def set5():
    ednum.setText(f"{ednum.text()}5")
def set6():
    ednum.setText(f"{ednum.text()}6")
def set7():
    ednum.setText(f"{ednum.text()}7")
def set8():
    ednum.setText(f"{ednum.text()}8")
def set9():
    ednum.setText(f"{ednum.text()}9")
def setplus():
    ednum.setText(f"{ednum.text()}+")
def setmin():
    ednum.setText(f"{ednum.text()}-")
def setkali():
    ednum.setText(f"{ednum.text()}*")
def setbagi():
    ednum.setText(f"{ednum.text()}/")
def clear():
    ednum.setText("")
def sethasil():
    x = eval(ednum.text())
    ednum.setText(f"{x}")

deflist = [set0, set1, set2, set3, set4, set5, set6, set7, set8, set9, setplus, setmin, setkali, setbagi]
btn: QPushButton = []

for i in range(10):
    qbtn = buat_tombol(str(i))
    qbtn.clicked.connect(deflist[i])
    btn.append(qbtn)

btn_clear = buat_tombol("C")
btn_clear.clicked.connect(clear)

btn_kurang = buat_tombol("-")
btn_kurang.clicked.connect(setmin)
btn_tambah = buat_tombol("+")
btn_tambah.clicked.connect(setplus)

btn_kali = buat_tombol("*")
btn_kali.clicked.connect(setkali)
btn_bagi = buat_tombol("/")
btn_bagi.clicked.connect(setbagi)

btn_hasil = buat_tombol("=")
btn_hasil.clicked.connect(sethasil)

grid.addWidget(ednum, 0,0,1,4)
grid.addWidget(btn_clear, 1, 3)
grid.addWidget(btn_kurang, 2, 3)
grid.addWidget(btn_tambah, 3, 3)
grid.addWidget(btn_kali, 4, 0)
grid.addWidget(btn_bagi, 4, 2)
grid.addWidget(btn_hasil, 4, 3)

grid.addWidget(btn[7], 1, 0)
grid.addWidget(btn[8], 1, 1)
grid.addWidget(btn[9], 1, 2)

grid.addWidget(btn[4], 2, 0)
grid.addWidget(btn[5], 2, 1)
grid.addWidget(btn[6], 2, 2)

grid.addWidget(btn[1], 3, 0)
grid.addWidget(btn[2], 3, 1)
grid.addWidget(btn[3], 3, 2)

grid.addWidget(btn[0], 4, 1)
widget = QWidget()
widget.setLayout(grid)
window.setCentralWidget(widget)

window.show()
app.exec_()