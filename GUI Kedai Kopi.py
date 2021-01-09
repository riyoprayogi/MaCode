from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("Pemesanan Kopi")
window.setGeometry(300, 300, 350, 400)

#Jenis Kopi
lbl_kopi = QLabel("Jenis Kopi:", window)
lbl_kopi.move(10, 10)
lbl_kopi.adjustSize()

cbx_kopi = QComboBox(window)
cbx_kopi.addItems(['Espresso (Rp. 25.000)', 'Macchiato (Rp. 30.000)', 'Cappucino (Rp. 35.000)', 'Latte (Rp. 35.000)'])
harga_kopi_indeks = [25000, 30000, 35000, 35000]
cbx_kopi.adjustSize()
cbx_kopi.move(100, 10)

#Topping tambahan
lbl_toppings = QLabel("Topping Tambahan:", window)
lbl_toppings.adjustSize()
lbl_toppings.move(10, 50)

chx_coklat = QCheckBox('Bubuk Coklat (Rp. 5.000)', window)
chx_coklat2 = QCheckBox('Serpihan Coklat (Rp. 8.000)', window)
chx_biskuit = QCheckBox('Biskuit (Rp. 8.000)', window)
chx_keju = QCheckBox('Serutan Keju (Rp. 7.000)', window)
chx_kayu_manis = QCheckBox('Kayu Manis (Rp. 4.500)', window)
chx_vanilla_cream = QCheckBox('Es Krim Vaninlla (Rp. 15500)', window)

chx_coklat.adjustSize()
chx_coklat2.adjustSize()
chx_biskuit.adjustSize()
chx_keju.adjustSize()
chx_kayu_manis.adjustSize()
chx_vanilla_cream.adjustSize()

chx_coklat.move(10, 80)
chx_coklat2.move(10, 110)
chx_biskuit.move(10, 140)
chx_keju.move(10, 170)
chx_kayu_manis.move(10, 200)
chx_vanilla_cream.move(10, 230)

#Fungsi menghitung total harga
def get_total_topping():
    total = 0
    if(chx_coklat.isChecked()):
        total += 5000
    if(chx_coklat2.isChecked()):
        total += 8000
    if(chx_biskuit.isChecked()):
        total += 8000
    if(chx_keju.isChecked()):
        total += 7000
    if(chx_kayu_manis.isChecked()):
        total += 4500
    if(chx_vanilla_cream.isChecked()):
        total += 15500
    return total

def hitung():
    harga_kopi = harga_kopi_indeks[cbx_kopi.currentIndex()]
    harga_topping = get_total_topping()
    total_harga = harga_kopi+harga_topping
    lbl_total.setText(f"Rp. {total_harga}")
    lbl_total.adjustSize()

#Tombol Harga
btn_hitung = QPushButton("Hitung", window)
btn_hitung.move(70, 270)
btn_hitung.clicked.connect(hitung)

#Label Harga
lbl_harga = QLabel("Harga:", window)
lbl_harga.adjustSize()
lbl_harga.move(10,310)

font_total = QFont()
font_total.setBold(True)
font_total.setPointSize(14)

lbl_total = QLabel(window)
lbl_total.setFont(font_total)
lbl_total.move(10,350)

window.show()
app.exec_()