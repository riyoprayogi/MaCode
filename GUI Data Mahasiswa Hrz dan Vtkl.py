from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon

import sys
app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Layout Horizontal dan Vertikal")
window.setGeometry(300, 300, 400, 200)

lbl_nama = QLabel("Nama", window)
lbl_nama.adjustSize()
lbl_nim = QLabel("Nim", window)
lbl_nim.adjustSize()
lbl_tgl_lahir = QLabel("Tgl. Lahir", window)
lbl_tgl_lahir.adjustSize()

ledit_nama = QLineEdit(window)
ledit_nim = QLineEdit(window)

calender_lahir = QCalendarWidget(window)

btn_simpan = QPushButton("Simpan", window)
btn_simpan.setIcon(QIcon("simpan.png"))
btn_simpan.setMinimumSize(QSize(200, 50))
btn_simpan.setIconSize(QSize(40,40))

layout_hor1 = QHBoxLayout()
layout_hor1.addWidget(lbl_nama)
layout_hor1.addWidget(ledit_nama)
layout_hor1.setSpacing(75)

layout_hor2 = QHBoxLayout()
layout_hor2.addWidget(lbl_nim)
layout_hor2.addWidget(ledit_nim)
layout_hor2.setSpacing(87)

layout_hor3 = QHBoxLayout()
layout_hor3.addWidget(lbl_tgl_lahir)
layout_hor3.addWidget(calender_lahir)
layout_hor3.setSpacing(50)

layout_hor4 = QVBoxLayout()
layout_hor4.addWidget(btn_simpan, alignment=Qt.AlignRight)
# layout_hor4.set

layout_ver = QVBoxLayout()
layout_ver.addLayout(layout_hor1)
layout_ver.addLayout(layout_hor2)
layout_ver.addLayout(layout_hor3)
layout_ver.addLayout(layout_hor4)

widget =QWidget()
widget.setLayout(layout_ver)
window.setCentralWidget(widget)

#Message Box
def show_message():
    #sd = selected date
    sd = calender_lahir.selectedDate()
    message_box = QMessageBox(window)
    message_box.setWindowTitle("Berhasil")
    message_box.setText(f"Nama: {ledit_nama.text()}\nNIM:{ledit_nim.text()}\nTanggal Lahir: {sd.totring()}atau{sd.day()}/{sd.month()}/{sd.year()}")
    message_box.exec_()

btn_simpan.clicked.connect(show_message)

window.show()
sys.exit(app.exec_())