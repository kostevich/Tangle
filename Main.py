#!/usr/bin/python

from PyQt6.QtWidgets import QApplication, QMainWindow, QLayoutItem

# Создание приложения.
Tangle = QApplication([])

# Создание интерфейса приложения на основе класса QMainWindow.
class MainWindow(QMainWindow):
    # Конструирование интерфейса приложения.
    def __init__(self):
        super(MainWindow, self).__init__()
        # Имя приложения.
        self.setWindowTitle("Tangle")

# Создание окошка.
window = MainWindow()
# Отображение окошка.
window.show()

# Обработка событий происходящих в окошке.
Tangle.exec()