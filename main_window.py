from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout


class main_window(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
        #configurando Layout
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

        

        #Nome da Janela/Projeto
        self.setWindowTitle('Calculator')

        #Ajustando os tamanhos de widgets à tela
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())