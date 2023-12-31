import pygame as pg
from PyQt5 import uic, QtWidgets
import menus.jogo as jogo

app = QtWidgets.QApplication([])
menuPrincipal = uic.loadUi("assets/menu.ui")
palavra = uic.loadUi("assets/palavra.ui")

def run_Menu():
    menuPrincipal.vsPc.clicked.connect(open_vsPC)
    menuPrincipal.vsJogador.clicked.connect(open_vsJogador)
    menuPrincipal.sair.clicked.connect(menuPrincipal.close)
    menuPrincipal.show()
    #app.exec() esse comando só pode ser utilizado uma vez só no programa
    #app.quit()

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

def main():
    run_Menu()
    app.exec()

if __name__ == '__main__':
    main()