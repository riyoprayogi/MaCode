import sys
from PyQt5.QtWidgets import *
app = QApplication([])

window = QMainWindow()
window.setMaximumHeight(500)
window.setMaximumWidth(800)
window.setGeometry(500, 200, 800, 500)
window.setWindowTitle("Data Harga Barang")

table = QTableWidget(window)
table.setGeometry(1, 1, 800, 500)
table.setColumnCount(3)
table.setRowCount(1)
table.setColumnWidth(0, 250)
table.setColumnWidth(1, 250)

judul1 = QTableWidget(table)
judul1.setGeometry(16, 1, 250, 25)
barang = QLabel(judul1)
barang.setText("Nama Barang")
barang.move(80, 5)

judul2 = QTableWidget(table)
judul2.setGeometry(265, 1, 250, 25)
harga = QLabel(judul2)
harga.setText("Harga Barang(Rp)")
harga.move(80, 5)

judul3 = QTableWidget(table)
judul3.setGeometry(515, 1, 100, 25)
jumlah = QLabel(judul3)
jumlah.setText("Jumlah Barang")
jumlah.move(10, 5)

tombol_tambah = QPushButton(window)
tombol_tambah.move(650, 30)
tombol_tambah.setText("Tambah Tabel")
tombol_hapus = QPushButton(window)
tombol_hapus.move(650, 60)
tombol_hapus.setText("Hapus Tabel\nSebelumnya")

def tambah_tabel():
    table.insertRow(0)
def hapus_tabel():
    table.removeRow(1)

tombol_tambah.clicked.connect(tambah_tabel)
tombol_hapus.clicked.connect(hapus_tabel)

window.show()
sys.exit(app.exec_())