from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                            QHBoxLayout, QMessageBox)
import sys

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.button = QPushButton("Exibir mensagem")
        self.line_edit = QLineEdit()
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.exibir)  # connection activated

    def exibir(self):
        self.text = self.line_edit.text()
        self.messsage_box = QMessageBox.information(self, "Exemplo 1",
                                                    self.text)

root = QApplication([])
app = Window()
app.show()
sys.exit(root.exec_())