from PySide6.QtWidgets import QLineEdit
from styles import BIG_FONT_SIZE, MARGIN_TEXT, MINIMUN_WIDTH
from PySide6.QtCore import Qt

class Display(QLineEdit):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [MARGIN_TEXT for _ in range(4)]
        self.setStyleSheet(f'font-size:{BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)