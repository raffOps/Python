from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                            QHBoxLayout, QMessageBox, QRadioButton, QGroupBox,
                            QVBoxLayout,QLabel,QFileDialog)

from PyQt5.Qt import (Qt,QPixmap)

import sys

class CustomLabel(QLabel):
    def __init__(self, parent=None):
        super(CustomLabel, self).__init__(parent)
        self.setMouseTracking(True)

    def mousePressEvent(self, e):
        img, re = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", filter="All(*.png *.jpg)")
        if re:
            self.setPixmap(QPixmap(img).scaled(800, 800, Qt.KeepAspectRatio))

class HandlerWindow(QWidget):
    def __init__(self, parent=None):
        super(HandlerWindow, self).__init__()
        self.resize(800,650)
        self.label = CustomLabel(self)
        self.label.setPixmap(QPixmap("imagem.jpg").scaled(800,800, Qt.KeepAspectRatio))

    def mouseMoveEvent(self, e):
        QApplication.setOverrideCursor(Qt.PointingHandCursor)

    def leaveEvent(self, e):
        QApplication.setOverrideCursor(Qt.ArrowCursor)


root = QApplication([])
app = HandlerWindow()
app.show()
sys.exit(root.exec_())