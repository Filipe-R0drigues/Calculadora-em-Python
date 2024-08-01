#from PySide6.QtCore import Qt
import sys
from info import Info
from display import Display
from PySide6.QtGui import QIcon
from main_window import main_window
from PySide6.QtWidgets import QApplication
from styles import setupTheme, WINDON_ICON_PATH
from buttons import ButtonsGrid


if __name__ == '__main__':
    #Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = main_window()
    #Definir icone
    icon = QIcon(str(WINDON_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    #Info
    info = Info('Sua Conta!')
    window.addToVLayout(info)

    #adicionando o display
    display = Display()
    window.addToVLayout(display)

    #adicionando novo layout
    buttons_grid = ButtonsGrid(display, info)
    buttons_grid._makeGrid()
    window.vLayout.addLayout(buttons_grid)

    #Ajustando os tamnhos à aplicação
    window.adjustFixedSize()

    #exibindo a aplicação
    window.show()
    app.exec()