import sys
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QVBoxLayout,
                             QLineEdit,
                             QPushButton,
                             QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()

    def __make(self):
        self.setWindowTitle("Calculadora")
        self.setGeometry(300, 300, 300, 200)

    def __add_text(self, layout, text, font="Arial", size=24):
        label = QLabel(text, self)
        font_element = QFont(font, size)
        label.setFont(font_element)
        label.setGeometry(0, 0, 400, 300)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        return label

    def __add_button(self, layout, text, function):
        button = QPushButton(text, self)
        button.clicked.connect(function)
        layout.addWidget(button)

    def __add_input(self, layout, placeholder):
        input_field = QLineEdit(self)
        input_field.setPlaceholderText(placeholder)
        layout.addWidget(input_field)

        return input_field

    def __add_widgets(self):
        layout = QVBoxLayout()

        self.header = self.__add_text(layout, "Calculadora")
        self.results = self.__add_text(layout, "", size=12)

        placeholder = "Digite uma expressão com + - * ou /"
        self.input_field = self.__add_input(layout, placeholder)

        self.__add_button(layout, "Calcular", self.__calc)
        self.__add_button(layout, "Fechar", self.close)

        self.setLayout(layout)

    def __calc(self):
        self.expression = self.input_field.text()

        # Calculations

        self.results.setText(self.expression)

    def run(self):
        self.__make()
        self.__add_widgets()

        self.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = Window()
    app.run()
