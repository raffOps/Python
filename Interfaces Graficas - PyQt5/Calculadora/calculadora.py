#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,QVBoxLayout,QHBoxLayout,QMessageBox)
import sys

class main_window(QWidget):
    def __init__(self):
        super(main_window,self).__init__()
        self.settings()
        self.create_widget()
        self.set_layout()
        self.primeiro_operando = []
        self.segundo_operando = []
        self.operador = None
        self.easteregg = 0

    def settings(self):
        self.resize(200,200)
        self.setWindowTitle("Calculadora")

    def create_widget(self):
        self.btn_0 = QPushButton("0",self)
        self.btn_1 = QPushButton("1")
        self.btn_2 = QPushButton("2")
        self.btn_3 = QPushButton("3")
        self.btn_4 = QPushButton("4")
        self.btn_5 = QPushButton("5")
        self.btn_6 = QPushButton("6")
        self.btn_7 = QPushButton("7")
        self.btn_8 = QPushButton("8")
        self.btn_9 = QPushButton("9")
        self.btn_mul = QPushButton("X")
        self.btn_div = QPushButton("/")
        self.btn_min = QPushButton("-")
        self.btn_plus = QPushButton("+")
        self.btn_equ = QPushButton("=")
        self.btn_eraseAll = QPushButton("C")
        self.btn_erase = QPushButton("<-")
        self.display = QLabel()

        self.btn_0.clicked.connect(lambda: self.analisar_equacao("0"))
        self.btn_1.clicked.connect(lambda: self.analisar_equacao("1"))
        self.btn_2.clicked.connect(lambda: self.analisar_equacao("2"))
        self.btn_3.clicked.connect(lambda: self.analisar_equacao("3"))
        self.btn_4.clicked.connect(lambda: self.analisar_equacao("4"))
        self.btn_5.clicked.connect(lambda: self.analisar_equacao("5"))
        self.btn_6.clicked.connect(lambda: self.analisar_equacao("6"))
        self.btn_7.clicked.connect(lambda: self.analisar_equacao("7"))
        self.btn_8.clicked.connect(lambda: self.analisar_equacao("8"))
        self.btn_9.clicked.connect(lambda: self.analisar_equacao("9"))
        self.btn_div.clicked.connect(lambda: self.analisar_equacao("/"))
        self.btn_mul.clicked.connect(lambda: self.analisar_equacao("*"))
        self.btn_min.clicked.connect(lambda: self.analisar_equacao("-"))
        self.btn_plus.clicked.connect(lambda: self.analisar_equacao("+"))
        self.btn_equ.clicked.connect(lambda: self.analisar_equacao("="))
        self.btn_eraseAll.clicked.connect(lambda: self.analisar_equacao("k"))
        self.btn_erase.clicked.connect(lambda: self.analisar_equacao("z"))

    def set_layout(self):
        self.layout_1 = QHBoxLayout()
        self.layout_1.addWidget(self.btn_0)
        self.layout_1.addWidget(self.btn_1)
        self.layout_1.addWidget(self.btn_2)
        self.layout_1.addWidget(self.btn_3)
        self.layout_1.addWidget(self.btn_4)

        self.layout_2 = QHBoxLayout()
        self.layout_2.addWidget(self.btn_5)
        self.layout_2.addWidget(self.btn_6)
        self.layout_2.addWidget(self.btn_7)
        self.layout_2.addWidget(self.btn_8)
        self.layout_2.addWidget(self.btn_9)

        self.layout_3 = QHBoxLayout()
        self.layout_3.addWidget(self.btn_equ)
        self.layout_3.addWidget(self.btn_plus)
        self.layout_3.addWidget(self.btn_min)
        self.layout_3.addWidget(self.btn_mul)
        self.layout_3.addWidget(self.btn_div)
        self.layout_3.addWidget(self.btn_eraseAll)
        self.layout_3.addWidget(self.btn_erase)

        self.layout_master=QVBoxLayout()
        self.layout_master.addWidget(self.display)
        self.layout_master.addLayout(self.layout_3)
        self.layout_master.addLayout(self.layout_2)
        self.layout_master.addLayout(self.layout_1)

        self.setLayout(self.layout_master)

    def analisar_equacao(self, digito):
        if digito == "k":
            self.display.clear()
            self.operador = None
            del (self.segundo_operando)
            self.segundo_operando = []
            del (self.primeiro_operando)
            self.primeiro_operando = []
            self.operador = None

        elif digito == "z" and (len(self.primeiro_operando) > 0 or len(self.segundo_operando) > 0):
            if self.operador == None:
                del(self.primeiro_operando[-1])
                print(self.primeiro_operando)
                self.display.setText(''.join(self.primeiro_operando))
            else:
                del (self.segundo_operando[-1])
                self.display.setText(''.join(self.segundo_operando))

        elif digito in "0123456789":
            if self.operador == None:
                self.primeiro_operando.append(digito)
                print(self.primeiro_operando)
                self.display.setText(''.join(self.primeiro_operando))
            else:
                self.segundo_operando.append(digito)
                self.display.setText(''.join(self.segundo_operando))
                print(self.segundo_operando)
        elif digito in "/*-+" and self.operador == None:
            self.operador = digito
            self.primeiro_operando = int(''.join(self.primeiro_operando))

        elif digito == "=":
            if self.operador != None:
                self.segundo_operando = int(''.join(self.segundo_operando))
                if self.operador == "+":
                    self.primeiro_operando += self.segundo_operando
                elif self.operador == '-':
                    self.primeiro_operando -= self.segundo_operando
                elif self.operador == "*":
                    self.primeiro_operando *= self.segundo_operando
                else:
                    if (self.segundo_operando != 0):
                        self.primeiro_operando //= self.segundo_operando
                    else:
                        QMessageBox.warning(self, "Erro", "Divisão por 0")

                self.primeiro_operando=str(self.primeiro_operando)
                self.display.setText(self.primeiro_operando)
                del(self.segundo_operando)
                self.segundo_operando = []
                del (self.primeiro_operando)
                self.primeiro_operando = []
                self.operador = None


if __name__ == "__main__":
    root = QApplication([])
    app = main_window()
    app.show()
    sys.exit(root.exec_())
