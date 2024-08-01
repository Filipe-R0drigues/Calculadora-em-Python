from pathlib import Path
import qdarkstyle

ROOT_DIR= Path(__file__).parent
FILES_DIR= ROOT_DIR / 'files'
WINDON_ICON_PATH = FILES_DIR / 'calculadora.jpg'  

#size-font
BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 16

MARGIN_TEXT = 15
MINIMUN_WIDTH = 500

PRIMARY_COLOR= '#1e81b0'
DARKER_PRIMARY_COLOR= '#16658a'
DARKEST_PRIMARY_COLOR= '#115270'

def isValidNumber(string : str ):
    valid = False
    try:
        float(string)
        valid = True
    except:
        ...
    return valid


qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}"""

def setupTheme(app):
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    app.setStyleSheet(app.styleSheet() + qss)
