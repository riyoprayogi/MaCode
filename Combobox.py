from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
app = QApplication([])

window = QMainWindow()
window.setGeometry(300,300,700,500)
window.setWindowTitle("Aplikasi Radio Button")

label_ukuran = QLabel("Ukuran Baju Anda:", window)
label_ukuran.adjustSize()
label_ukuran.move(50,10)

radio_ukuran_S = QRadioButton("Small", window)
radio_ukuran_M = QRadioButton("Medium", window)
radio_ukuran_L = QRadioButton("Large",window)
radio_ukuran_XL = QRadioButton("Extra Large", window)
radio_ukuran_S.setChecked(True)
radio_ukuran_XL.adjustSize()
radio_ukuran_S.move(50, 50)
radio_ukuran_M.move(50, 80)
radio_ukuran_L.move(50, 110)
radio_ukuran_XL.move(50, 140)

radio_group_ukuran = QButtonGroup(window)
radio_group_ukuran.addButton(radio_ukuran_S)
radio_group_ukuran.addButton(radio_ukuran_M)
radio_group_ukuran.addButton(radio_ukuran_L)
radio_group_ukuran.addButton(radio_ukuran_XL)

def click_ukuran(btn):
    label_hasil.setText(f"ukuran : {btn.text} & Metode Pembayaran : {radio_group_metode.checkedButton().text()}")
    label_hasil.adjustSize()

def click_metode(btn):
    label_hasil.setText(f"ukuran : {radio_group_ukuran.checkedButton().text()} & Metode Pembayaran : {btn.text()}")
    label_hasil.adjustSize()

radio_group_ukuran.buttonClicked.connect(click_ukuran)

label_metode =QLabel("Metode Pembayaran :", window)
label_metode.move(50, 200)
label_metode.adjustSize()

radio_metode_debcre = QRadioButton("Debit/Kartu Kredit", window)
radio_metode_transfer =QRadioButton("Transfer Bank", window)
radio_metode_cod = QRadioButton("Cash On Delivery", window)
radio_metode_debcre.setChecked(True)
radio_metode_debcre.adjustSize()
radio_metode_transfer.adjustSize()
radio_metode_cod.adjustSize()

radio_group_metode = QButtonGroup(window)
radio_group_metode.addButton(radio_metode_debcre)
radio_group_metode.addButton(radio_metode_transfer)
radio_group_metode.addButton(radio_metode_cod)

radio_metode_debcre.move(50, 230)
radio_metode_transfer.move(50, 260)
radio_metode_cod.move(50, 290)

radio_group_metode.buttonClicked.connect(click_metode)

font_ku = QFont("Verdana")
font_ku.setPointSize(8)
font_ku.setBold(True)
label_hasil = QLabel("", window)
label_hasil.move(50, 360)
label_hasil.setFont(font_ku)

window.show()
app.exec_()