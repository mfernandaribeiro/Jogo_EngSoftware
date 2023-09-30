import pygame
from PyQt5 import uic, QtWidgets
import random
import menus.menuPrincipal
import re

app = QtWidgets.QApplication([])

login_screen = uic.loadUi("assets/login.ui")
register_screen = uic.loadUi("assets/cadastro.ui")
#recover_screen = uic.loadUi("assets/recpass_screen.ui")
#code_screen = uic.loadUi("assets/code_screen.ui")
#newpass_screen = uic.loadUi("assets/chargepass_screen.ui")

def run_login(): 
    login_screen.pushButton_6.clicked.connect(login)
    login_screen.pushButton_5.clicked.connect(open_register_screen)
    register_screen.cadastrarBotao.clicked.connect(register)
    register_screen.pushButton_6.clicked.connect(open_login_screen)


    login_screen.show()
    app.exec()
    app.quit()

def open_login_screen():
    register_screen.close()
    login_screen.show()

def login():
    login_screen.label_3.setText("")
    username = login_screen.usuario.text()
    password = login_screen.usuario_2.text()
    
    if username == "" or password == "":
        login_screen.label_3.setText("Preencha todos os campos!")
        return
    elif user.login(username, password):
        login_screen.label_3.setText("Login realizado com sucesso!")
        login_screen.close()
        menus.menuPrincipal.run_menu()
    else:
        login_screen.label_3.setText("Usuário ou senha incorretos!")

def open_register_screen():
    login_screen.close()
    register_screen.show()

def register():
    register_screen.label_5.setText("")
    register_screen.label_6.setText("")
    register_screen.label_7.setText("")
    register_screen.label_8.setText("")
    
    username = register_screen.usuario.text()
    username = register_screen.usuario.text()
    email = register_screen.email.text()
    password = register_screen.senha_2.text()
    password2 = register_screen.senha_3.text()
    
    # Regex to check if the email is valid
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(regex, email):
        register_screen.label_7.setText("Email inválido!")
        return
    else:
        result = user.register(username, email, password, password2)
    
        if result == "Usuário cadastrado com sucesso!":
            register_screen.close()
            login_screen.show()
            login_screen.label_3.setText(result)
        else:
            error_labels = {
                "o Username já está sendo usado!": register_screen.label_6,
                "Este email já está sendo usado, tente outro!": register_screen.label_7,
                "Preencha todos os campos!": register_screen.label_5,
                "As senhas não coincidem!": register_screen.label_8,
            }
            error_label = error_labels[result]
            if error_label:
                error_label.setText(result)