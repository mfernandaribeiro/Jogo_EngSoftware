import pygame as pg
from PyQt5 import uic, QtWidgets
from jogo import main

app = QtWidgets.QApplication([])
menuPrincipal = uic.loadUi("../assets/menu.ui")

def run_Menu():
    menuPrincipal.vsPc.clicked.connect(open_vsPC)
    menuPrincipal.vsJogador.clicked.connect(open_vsJogador)
    menuPrincipal.sair.clicked.connect(menuPrincipal.close)
    menuPrincipal.show()
    app.exec()
    app.quit()

def open_vsPC():
    menuPrincipal.close()
    main('PC')

def open_vsJogador():
    menuPrincipal.close()
    main('Jogador')

run_Menu()