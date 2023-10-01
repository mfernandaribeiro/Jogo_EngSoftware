import pygame
from PyQt5 import uic, QtWidgets
from jogo import main

app = QtWidgets.QApplication([])
menuPrincipal = uic.loadUi("../assets/menu.ui")
pontuacao_screen = uic.loadUi("../assets/pontuacao.ui")

def run_Menu():
    #menuPrincipal.vsPC.clicked.connect(open_vsPC('PC'))
    menuPrincipal.vsJogador.clicked.connect(lambda:main('PC'))
    menuPrincipal.pontuacao.clicked.connect(open_pontuacao_screen)
    menuPrincipal.sair.clicked.connect(menuPrincipal.close)
    menuPrincipal.show()
    app.exec()
    app.quit()

def open_pontuacao_screen():
    menuPrincipal.close()
    pontuacao_screen.show()

run_Menu()