from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])

window = QMainWindow()
window.setGeometry(500, 300, 500, 150)
window.setWindowTitle("Aplikasi Pertama")

label_masuk = QLabel(window)
label_masuk.setText("Masukan Nama : ")
label_masuk.setFixedWidth(150)
label_masuk.move(20,20)

#ledit = Line Edit
ledit_nama = QLineEdit(window)
ledit_nama.setText('Nama Anda')
ledit_nama.setToolTip('silahkan masukan nama anda')
ledit_nama.move(150,20)
ledit_nama.setFixedWidth(300)

# ledit_nama.setEchoMode(QQLineEdit.Password)
button_ok = QPushButton(window)
button_ok.setText("Ok")
button_ok.move(350,70)

def button_act():
    isi_field = ledit_nama.text()
    message_box = QMessageBox(window)
    message_box.setWindowTitle("Informasi")
    message_box.setText(f"Nama anda adalah : {isi_field}")
    message_box.exec_()

button_ok.clicked.connect(button_act)

window.show()
app.exec_()

