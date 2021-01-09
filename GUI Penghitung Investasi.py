import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__(1, 2)
        self.setHorizontalHeaderLabels(['Nama barang','harga barang'])
        self.verticalHeader().setDefaultSectionSize(25)
        self.horizontalHeader().setDefaultSectionSize(270)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def tambah(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount)

    def _removeRow(self):
        if self.rowCount() > 0:
            self.removeRow(self.rowCount() - 1)

    def _copyRow(self):
        self.insertRow(self.rowCount())
        rowCount = self.rowCount()
        columnCount = self.columnCount()
        for j in range(columnCount):
            if not self.item(rowCount - 2, j) is None:
                self.setItem(rowCount - 1, j, QTableWidgetItem(self.item(rowCount - 2, j).text()))

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        mainLayout = QHBoxLayout()
        table = TableWidget()
        mainLayout.addWidget(table)
        buttonLayout = QVBoxLayout()

        button_new = QPushButton('Tambah')
        button_new.clicked.connect(table.tambah)
        buttonLayout.addWidget(button_new)
        button_copy = QPushButton('Copy')
        button_copy.clicked.connect(table._copyRow)
        buttonLayout.addWidget(button_copy)

        button_remove = QPushButton('Hapus')
        button_remove.clicked.connect(table._removeRow)
        buttonLayout.addWidget(button_remove, alignment=Qt.AlignTop)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)

app = QApplication(sys.argv) ; app.setStyleSheet('QPushButton{font-size: 20px; width: 200px; height: 50px}')
demo = AppDemo() ; demo.show() ; sys.exit(app.exec_())