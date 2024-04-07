
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QDialog


class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Tangle")
        # self.setGeometry(100, 100, 200, 100)
        label = QLabel('This is the second window', self)
        label.move(50, 30)
        