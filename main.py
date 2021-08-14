import sys
from PyQt5.QtWidgets import *
from interface import Ui_Window

current_expression = ""
current_number = ""
operator = ""
first_number = 0


class Window(QMainWindow, Ui_Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Bind numbers
        self.button_1.pressed.connect(lambda: self.addNumber('1'))
        self.button_2.pressed.connect(lambda: self.addNumber('2'))
        self.button_3.pressed.connect(lambda: self.addNumber('3'))
        self.button_4.pressed.connect(lambda: self.addNumber('4'))
        self.button_5.pressed.connect(lambda: self.addNumber('5'))
        self.button_6.pressed.connect(lambda: self.addNumber('6'))
        self.button_7.pressed.connect(lambda: self.addNumber('7'))
        self.button_8.pressed.connect(lambda: self.addNumber('8'))
        self.button_9.pressed.connect(lambda: self.addNumber('9'))
        self.button_0.pressed.connect(lambda: self.addNumber('0'))

        # Bind actions
        self.button_div.pressed.connect(lambda: self.action('/'))
        self.button_mul.pressed.connect(lambda: self.action('*'))
        self.button_minus.pressed.connect(lambda: self.action('-'))
        self.button_plus.pressed.connect(lambda: self.action('+'))
        self.button_eq.pressed.connect(lambda: self.equally())
        self.button_clear.pressed.connect(lambda: self.clear())

    def refreshDisplay(self):
        if current_expression:
            self.display.setText(current_expression)
        else:
            self.display.setText("0")

    def addNumber(self, num):
        global current_expression, current_number
        current_expression = current_expression + num
        current_number = current_number + num

        self.refreshDisplay()

    def action(self, oper):
        global operator, first_number, current_expression, current_number
        if current_expression:
            if operator:
                if current_number:
                    self.equally()
                else:
                    operator = oper
                    current_expression = current_expression[:-1] + oper
                    self.refreshDisplay()
            else:
                first_number = float(current_number)
                current_number = ""
                operator = oper
                current_expression = current_expression + oper
                self.refreshDisplay()

    def equally(self):
        global first_number, operator, current_number, current_expression
        if first_number and operator and current_number:
            first_number, current_number = float(first_number), float(current_number)
            if operator == "/" and current_number != 0:
                resl = first_number / current_number
            elif operator == "*":
                resl = first_number * current_number
            elif operator == "+":
                resl = first_number + current_number
            elif operator == "-":
                resl = first_number - current_number
            current_expression = str(resl)
            current_number = str(resl)
            operator = ""
            self.refreshDisplay()

    def clear(self):
        global current_expression, current_number, first_number, operator
        current_number = ""
        current_expression = ""
        first_number = 0
        operator = ""
        self.refreshDisplay()

    # Bind keys
    def keyPressEvent(self, e):
        key = e.key()
        if key == 49:
            self.addNumber('1')
        elif key == 50:
            self.addNumber('2')
        elif key == 51:
            self.addNumber('3')
        elif key == 52:
            self.addNumber('4')
        elif key == 53:
            self.addNumber('5')
        elif key == 54:
            self.addNumber('6')
        elif key == 55:
            self.addNumber('7')
        elif key == 56:
            self.addNumber('8')
        elif key == 57:
            self.addNumber('9')
        elif key == 48:
            self.addNumber('0')
        elif key == 47:
            self.action('/')
        elif key == 42:
            self.action('*')
        elif key == 45:
            self.action('-')
        elif key == 43:
            self.action('+')
        elif key in [16777221, 16777220]: #enter
            self.equally()
        elif key == 16777219: #backspace
            self.clear()




app = QApplication([])
win = Window()
win.show()
sys.exit(app.exec())