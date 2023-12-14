#!/usr/bin/python

#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods import CheckPythonMinimalVersion
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction 
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QListWidget, QMainWindow, QPushButton, QToolBar, QVBoxLayout, QWidget

#==========================================================================================#
# >>>>> ИНИЦИАЛИЗАЦИЯ СКРИПТА <<<<< #
#==========================================================================================#

# Проверка поддержки используемой версии Python.
CheckPythonMinimalVersion(3, 11)

#==========================================================================================#
# >>>>> ЧТЕНИЕ НАСТРОЕК <<<<< #
#==========================================================================================#

ListRepository = ("1", "2", "3", "4", "5",)
FunctionRepository = ("уДАИЛАСМВ", "2", )

#==========================================================================================#
# >>>>> ИНИЦИАЛИЗАЦИЯ ПРИЛОЖЕНИЯ <<<<< #
#==========================================================================================#

# Создание приложения.
Tangle = QApplication([])

#==========================================================================================#
# >>>>> СОЗДАНИЕ ПРИЛОЖЕНИЯ <<<<< #
#==========================================================================================#

# Создание интерфейса приложения на основе класса QMainWindow.
class MainWindow(QMainWindow):
    # Конструирование интерфейса приложения.
    def __init__(self):
        super(MainWindow, self).__init__()
        # Имя приложения.
        self.setWindowTitle("Tangle")
        
        # Создание подложки.
        self.LayoutLeft = QVBoxLayout()
        self.LayoutUnder = QHBoxLayout()

        # Создание названия окошка с репозиториями.
        self.Lable = QLabel("Repository", self)

        # Создание списка репозиториев.
        self.List = QListWidget(self)

        # Фиксированный размер окошка списка.
        self.List.setFixedSize(300, 500)

        # Добавление элементов списка.
        self.List.addItems(ListRepository)

        # Создание кнопочек для работы репозиториев.
        self.ButtonAdd = QPushButton("Добавить")
        self.ButtonDelete = QPushButton("Удалить")

        # Фиксированный размер кнопок.
        self.ButtonAdd.setFixedSize(120, 25)
        self.ButtonDelete.setFixedSize(120, 25)

        # Добавление кнопок на макет.
        self.LayoutUnder.addWidget(self.ButtonAdd)
        self.LayoutUnder.addWidget(self.ButtonDelete)

        # Растягиваем пространство за кнопочками.
        self.LayoutUnder.addStretch(0)

        # Добавление текста на основной макет.
        self.LayoutLeft.addWidget(self.Lable, alignment = Qt.AlignmentFlag.AlignVCenter)
        # Добавление списка на основной макет.
        self.LayoutLeft.addWidget(self.List)
    
        # Создание объекта класса виджет.
        widget = QWidget()

        # Добавление макета на виджет.
        widget.setLayout(self.LayoutLeft)

        # Преобразовать среднее положение для макета.
        self.setCentralWidget(widget)

        # Добавление дополнительного макета на основной.
        self.LayoutLeft.addLayout(self.LayoutUnder)

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

#==========================================================================================#
# >>>>> СОЗДАНИЕ ОКОШКА ПРИЛОЖЕНИЯ <<<<< #
#==========================================================================================#

# Создание окошка.
window = MainWindow()
# Отображение окошка.
window.show()

#==========================================================================================#
# >>>>> ОБРАБОТКА СОБЫТИЙ ПРИЛОЖЕНИЯ <<<<< #
#==========================================================================================#

# Обработка событий происходящих в окошке.
Tangle.exec()