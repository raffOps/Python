from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QGridLayout, QFileDialog,QVBoxLayout,QHBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

import sys

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.preview_screen = QApplication.primaryScreen().grabWindow(0)
        self.settings()
        self.create_widgets()
        self.set_layout()

    def settings(self):
        self.resize(800, 800)
        self.setWindowTitle("Screenshoter")

    def create_widgets(self):
        self.img_preview = QLabel()
        self.img_preview.setPixmap(self.preview_screen.scaled(800, 800, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.btn_save_screenshot= QPushButton("Save screenshot")
        self.btn_new_screenshot = QPushButton("New screenshot")

        # signals connections
        self.btn_save_screenshot.clicked.connect(self.save_screenshot)
        self.btn_new_screenshot.clicked.connect(self.new_screenshot)

    def set_layout(self):
        self.layout_options= QHBoxLayout()
        self.layout_options.addWidget(self.btn_new_screenshot)
        self.layout_options.addWidget(self.btn_save_screenshot)

        self.layout_master=QVBoxLayout()
        self.layout_master.addWidget(self.img_preview)
        self.layout_master.addLayout(self.layout_options)

        self.setLayout(self.layout_master)


    def save_screenshot(self):
        img, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo",
                                             filter="PNG(*.png);; JPEG(*.jpg)")
        if img[-3:] == "png":
            self.preview_screen.save(img, "png")
        elif img[-3:] == "jpg":
            self.preview_screen.save(img, "jpg")

    def new_screenshot(self):
        self.hide()
        QTimer.singleShot(1000, self.take_screenshot)

    def take_screenshot(self):
        self.preview_screen = QApplication.primaryScreen().grabWindow(0)
        self.img_preview.setPixmap(self.preview_screen.scaled(800, 800, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.show()

root = QApplication([])
app = MainWindow()
app.show()
sys.exit(root.exec_())


