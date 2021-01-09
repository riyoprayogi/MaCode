import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon

app = QApplication([])

window = QMainWindow()
window.setGeometry(450, 300, 500, 300)
window.setWindowTitle("Investasi anda")

labelKeluar = QLabel(window)
labelKeluar.setText("Jumlah Pengeluaran : ")
labelKeluar.adjustSize()
labelBunga = QLabel(window)
labelBunga.setText("Bunga(%) : ")
labelBunga.adjustSize()
labelTahun = QLabel(window)
labelTahun.setText("Tahun ke-: ")
labelTahun.adjustSize()

leditKeluar = QLineEdit(window)
leditKeluar.setText('')
leditBunga = QLineEdit(window)
leditBunga.setText('')
leditTahun = QLineEdit(window)
leditTahun.setText('')

btn_calculate = QPushButton('Calculate', window)
btn_calculate.setIcon(QIcon('Kalkulasi Investasi'))
btn_calculate.setMinimumSize(QSize(80, 20))
btn_calculate.setIconSize(QSize(230, 160))

labelResult = QLabel(window)
labelResult.move(130, 200)
labelResult.setFixedWidth(400)

layout_hor1 = QHBoxLayout()
layout_hor1.addWidget(labelKeluar)
layout_hor1.addWidget(leditKeluar)
layout_hor1.setSpacing(75)

layout_hor2 = QHBoxLayout()
layout_hor2.addWidget(labelBunga)
layout_hor2.addWidget(leditBunga)
layout_hor2.setSpacing(85)


layout_hor4 = QVBoxLayout()
layout_hor4.addWidget(btn_calculate, alignment=Qt.AlignLeft)
#layout_hor4.set

layout_ver = QHBoxLayout()
layout_ver.addLayout(layout_hor1)
layout_ver.addLayout(layout_hor2)
layout_ver.addLayout(layout_hor4)

def calculate():
    isiKeluar = leditKeluar.setText()
    isiKeluar = int(isiKeluar)
    isiBunga = leditBunga.setText()
    isiBunga = int(isiBunga)
    isiTahun = leditTahun.setText()
    isiTahun = int(isiTahun)
    if(isiTahun != 0 and isiKeluar !=0 and isiBunga !=0):
        isiResult = (isiKeluar*isiBunga/100+isiKeluar)*isiTahun
        isiResult = int(isiResult)
        labelResult.setText(f"Investasi anda selama {isiTahun}tahun menjadi RP. {isiResult}")

btn_calculate.clicked.connect(calculate)

window.show()
sys.exit(app.exec_())