import pygame as pg
from PyQt5 import uic, QtWidgets
from . import jogo

app = QtWidgets.QApplication([])
menuPrincipal = uic.loadUi("assets/menu.ui")
palavra = uic.loadUi("assets/palavra.ui")

def run_Menu():
    menuPrincipal.vsPc.clicked.connect(open_vsPC)
    menuPrincipal.vsJogador.clicked.connect(open_vsJogador)
    menuPrincipal.sair.clicked.connect(menuPrincipal.close)
    menuPrincipal.show()
    app.exec()
    app.quit()

def open_vsPC():
    menuPrincipal.close()
    jogo.main('PC',' ')

def open_vsJogador():
    #abrir tela digitar palavra
    palavra.show()
    menuPrincipal.close()
    palavra.pushButton.clicked.connect(vsJogador)

def vsJogador():
    palavra.label_2.setText("")
    input_text = palavra.lineEdit.text().upper() 
    
    if not input_text:
        palavra.label_2.setText("Preencha pelo menos uma palavra!")
        return
    else:
        palavras = input_text.split()
        jogo.main('Jogador', palavras)


if __name__ == '__main__':
    run_Menu()