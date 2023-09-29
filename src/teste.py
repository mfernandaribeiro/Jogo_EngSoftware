import pygame
from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
login_screen = uic.loadUi("assets/menu.ui")

login_screen.show()
app.exec()
app.quit()
