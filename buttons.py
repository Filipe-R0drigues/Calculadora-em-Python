import math
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from styles import MEDIUM_FONT_SIZE, isValidNumber
from display import Display
from info import Info

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75,75)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['c','<','^','/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['', '0','.','=']
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self.equation = ''
        self.numLeft = None
        self.numRight = None
        self.operator = None
        self._makeGrid()
    
    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for row_number, row in enumerate(self._gridMask):
            for colum_number, button_text in enumerate(row):
                button = Button(button_text)
                if button_text not in '0123456789':
                    button.setProperty('cssClass', 'SpecialButton')
                    self._configButtonSpecial(button)

                if button_text == '0':
                    self.addWidget(button, row_number, 0,1,2)
                else:
                    self.addWidget(button, row_number, colum_number)
                
                slot = self._makeSlot(self._insertButtonTextInDisplay, button)
                self._connectButtonClicked(button, slot)

    
    def _connectButtonClicked(self,  button, slot):
        button.clicked.connect(slot)
        
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot
    
    def _insertButtonTextInDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return
        else:
            self.display.insert(buttonText)    

    def _configButtonSpecial(self, button):
        text = button.text()
        if text in '+-c/*^':
            self._connectButtonClicked(
                button, self._makeSlot(self._operatorClicked, button))

        if text == 'c':
            self._connectButtonClicked(button,self._displayClear)
        
        if text == '=':
            self._connectButtonClicked(button,self._equal)
        
        if text == '<':
            self._connectButtonClicked(button, self.display.backspace)

    def _displayClear(self):
        self.equation = ''
        self.numLeft = None
        self.numRight = None
        self.operator = None
        self.display.clear()          

    def _operatorClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self.numLeft is None:
            return  
        
        if self.numLeft is None:
            self.numLeft = float(displayText)
        
        self.operator = buttonText
        self.equation = f'{self.numLeft} {self.operator}'
    
    def _equal(self, button):
        displayText = self.display.text()

        if not isValidNumber(displayText):
           print('Numero invalido!')
           self.display.clear()
           return

        # if self.numRight is None:
        self.numRight = float(displayText)
        self.equation = f'{self.numLeft} {self.operator} {self.numRight}'
        result = 'error'
        
        try:
            if '^' in self.equation and isinstance(self.numLeft, float):
                result = math.pow(self.numLeft, self.numRight)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            print('Não pode dividir por zero!')
        except OverflowError:
            print('Número muito grande!')

        
        self.info.setText(f'{self.equation} = {result}')
        self.display.clear()
        self.numLeft = result
        self.numRight = None

        if result == 'error':
            self.numLeft = None