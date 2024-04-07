#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from PyQt6.QtWidgets import QToolBar
from PyQt6.QtGui import QAction

#==========================================================================================#
# >>>>> ГЛАВНОЕ ОКНО <<<<< #
#==========================================================================================#

class ToolBar():

    #==========================================================================================#
    # >>>>> КОНСТРУКТОР <<<<< #
    #==========================================================================================#

    def __init__(self, window):
        
        # Создание панели инструментов.
        self.ToolBarObject = QToolBar()

        # Передаём данные класса MainWindow.
        self.window = window

    #==========================================================================================#
    # >>>>> ПАНЕЛЬ ИНСТРУМЕНТОВ <<<<< #
    #==========================================================================================#

    def CreateToolBar(self):
        # Создание кнопок на панели инструментов.
        FirstIcon = QAction("❤️", self.window)
        SecondIcon = QAction("❤️❤️❤️", self.window)

        # Добавление кнопок на панель инструментов.
        self.ToolBarObject.addAction(FirstIcon)
        self.ToolBarObject.addAction(SecondIcon)

        return self.ToolBarObject