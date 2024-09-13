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
        self.setWindowTitle('Exemplo PyQt5')
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
        self.button = QPushButton(text, self)
        self.button.clicked.connect(function)
        layout.addWidget(self.button)

    def __add_widgets(self):
        layout = QVBoxLayout()

        self.header = self.__add_text(layout, "Calculadora")
        self.results = self.__add_text(layout, "", size=12)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Digite uma expressão com + - * ou /")
        layout.addWidget(self.input_field)

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
