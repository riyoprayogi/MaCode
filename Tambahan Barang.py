from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("Tabel Barang")
window.setGeometry(300, 300, 400, 500)

lbl_barang = QLabel("<b>Daftar Barang :</b>", window)
lbl_barang_kayu = QLabel("1. Kayu Rp 5000", window)
lbl_barang_besi = QLabel("2. Besi Rp 10000", window)
lbl_barang_batu = QLabel("3. Batu Rp 8000",window)
lbl_barang.adjustSize()
lbl_barang_kayu.adjustSize()
lbl_barang_besi.adjustSize()
lbl_barang_batu.adjustSize()
lbl_barang.move(10, 15)
lbl_barang_kayu.move(15, 40)
lbl_barang_besi.move(15, 60)
lbl_barang_batu.move(15, 80)

label_masuk = QLabel(window)
label_masuk.setText("<b>Masukan Barang :</b> ")
label_masuk.setFixedWidth(150)
label_masuk.move(10,100)

table = QTableWidget(window)
table.setRowCount(3)
table.setColumnCount(2)
table.setFixedSize(250, 150)
table.move(30, 150)
table.setHorizontalHeaderLabels(["Tabel Barang", "Harga"])

table.setItem(0,0, QTableWidgetItem(" "))
table.setItem(0,1, QTableWidgetItem(" "))
table.setItem(1,0, QTableWidgetItem(" "))
table.setItem(1,1, QTableWidgetItem(" "))
table.setItem(2,0, QTableWidgetItem(" "))
table.setItem(2,1, QTableWidgetItem(" "))
table.adjustSize()

window.show()
app.exec_()

print(".:: Program Prediksi Investasi ::.\n")
saldo = int(input("Masukkan Saldo Awal (Rp.) : "))
persentase = float(input("Masukkan Persentase Keuntungan Per Tahunnya (%) : "))
tahun = int(input("Masukkan Waktu Investasi (Tahun) : "))
print("Tahun Ke-\t Saldo Awal\t\t Laba Investasi\t\t Saldo Akhir")
for i in range(tahun):
    laba = saldo*(persentase/100)
    saldoAkhir = saldo+laba
    print(f"{i}\t\t {saldo}\t\t\t {laba}\t\t\t {saldoAkhir}")
    saldo = saldoAkhir