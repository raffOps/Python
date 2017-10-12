#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,QVBoxLayout,QHBoxLayout,QMessageBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

import sys
import time


class main_window(QWidget):
    def __init__(self):
        super(main_window,self).__init__()
        self.settings()
        self.create_widget()
        self.set_layout()
        self.equacao=[]
        self.count_operator=0
        self.calcula_proximo=False
        self.operadores=["+", "-", "/", "x"]

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
        self.btn_mul.clicked.connect(lambda: self.analisar_equacao("x"))
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
        self.index_max = len(self.equacao) - 1
        if digito == "k":
            self.display.clear()
            self.equacao[:] = []
        elif digito == "z":
            del[self.equacao[-1]]
            self.display.setText(''.join(self.equacao))

        elif digito == "=":
            if not self.__verifica_inconsistencia():
                return
            else:
                self.__calcula_equacao()
        else:
            self.equacao.append(digito)
            self.display.setText(''.join(self.equacao))

    def __calcula_equacao(self):
        indice_operador=None
        for operador in self.operadores:
            if operador in self.equacao:
                indice_operador=self.equacao.index(operador)
                break
        #Divide a lista em duas partes, transforma cada numa string e depois converte pra int
        self.primeiro_operando = int(''.join(self.equacao[:indice_operador]))
        self.segundo_operando = int(''.join(self.equacao[indice_operador+1:]))

        if self.equacao[indice_operador] == "+":
            self.display.setText(str(self.primeiro_operando + self.segundo_operando))
        if self.equacao[indice_operador] == "-":
            self.display.setText(str(self.primeiro_operando - self.segundo_operando))
        if self.equacao[indice_operador] == "*":
            self.display.setText(str(self.primeiro_operando * self.segundo_operando))
        if self.equacao[indice_operador] == "/":
            if self.segundo_operando == 0:
                self.messsage_box=QMessageBox.warning(self,"Divisão por 0",self.txt)
            else:
                self.display.setText(str(self.primeiro_operando // self.segundo_operando))

    def __verifica_inconsitencia(self):

        if self.equacao[0] in self.operadores:
            self.messsage_box= QMessageBox.warning(self, "Erro: Equação iniciando com operadores", self.text)
            return False
        elif self.equacao[self.index_max] in self.operadores:
            self.messsage_box = QMessageBox.warning(self, "Erro: Equação terminando com operador", self.text)
            return False

        for indice in range(self.index_max + 1):
            if indice != 0 or indice != self.index_max:
                if ((self.equacao[indice - 1] in self.operadores or
                             self.equacao[indice + 1] in self.operadores) and
                            self.equacao[indice] in self.operadores):
                    self.messsage_box = QMessageBox.warning(self, "Erro: Dois operadores seguidos", self.text)
                    return False
            elif (indice == 0 and self.equacao[0] in self.operadores
                  and self.equacao[1] in self.operadores):
                self.messsage_box = QMessageBox.warning(self, "Erro: Dois operadores seguidos", self.text)
                return False

            elif (indice == self.index_max and self.equacao[self.index_max] in self.operadores
                  and self.equacao[self.index_max - 1] in self.operadores):
                self.messsage_box = QMessageBox.warning(self, "Erro: Dois operadores seguidos", self.text)
                return False
        return True

if __name__ == "__main__":
    root = QApplication([])
    app = main_window()
    app.show()
    sys.exit(root.exec_())











