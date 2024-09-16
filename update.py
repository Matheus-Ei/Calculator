import sys
import subprocess
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QVBoxLayout,
                             QLineEdit,
                             QPushButton,
                             QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from window import Window


class Update(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()

    def __make(self):
        self.setWindowTitle("Atualizador")
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

    def __dont_update(self):
        subprocess.Popen("source ./.venv/bin/activate && python3 ./window.py",
                         shell=True,
                         executable='/bin/bash',
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
        exit()

    def __add_widgets(self):
        layout = QVBoxLayout()

        self.header = self.__add_text(layout, "Update disponivel!")

        self.__add_text(layout, "Atualizar a calculadora?", size=8)
        self.__add_button(layout, "Sim", self.__relaunch)
        self.__add_button(layout, "Não", self.__dont_update)

        self.setLayout(layout)

    def __update(self):
        subprocess.run(['git', 'pull'])

    def __relaunch(self):
        self.__update()

        subprocess.Popen("source ./.venv/bin/activate && python3 ./app.py",
                         shell=True,
                         executable='/bin/bash',
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

        exit()

    def run(self):
        self.__make()
        self.__add_widgets()

        self.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = Update()
    app.run()
