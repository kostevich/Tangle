#!/usr/bin/python

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar

from PyQt6.QtGui import QAction

# Создание приложения.
Tangle = QApplication([])

# Создание интерфейса приложения на основе класса QMainWindow.
class MainWindow(QMainWindow):
    # Конструирование интерфейса приложения.
    def __init__(self):
        super(MainWindow, self).__init__()
        # Имя приложения.
        self.setWindowTitle("Tangle")
        
        Lable = QLabel("Repository", self)
        Lable.move(250, 100)

        # Создание панели инструментов.
        PanelMenu = QToolBar("Показать/Скрыть панель инструментов")
        # Создание кнопки на панели инструментов.
        Templates = QAction("Templates", self)
        ApplicationSettings = QAction("ApplicationSettings", self)
        # Добавление кнопки на панель.
        PanelMenu.addAction(Templates)
        PanelMenu.addAction(ApplicationSettings)
        # Отображение панели меню.
        self.addToolBar(PanelMenu)
        


# Создание окошка.
window = MainWindow()
# Отображение окошка.
window.show()

# Обработка событий происходящих в окошке.
Tangle.exec()