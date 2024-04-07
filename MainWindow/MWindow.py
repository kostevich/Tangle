#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from PyQt6 import QtGui
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow
from MainWindow.MenuBar import MenuBar
from MainWindow.ToolBar import ToolBar

#==========================================================================================#
# >>>>> ГЛАВНОЕ ОКНО <<<<< #
#==========================================================================================#

class MainWindow(QMainWindow):

    #==========================================================================================#
    # >>>>> КОНСТРУКТОР <<<<< #
    #==========================================================================================#
    
    # Конструирование интерфейса приложения.
    def __init__(self):
        super(MainWindow, self).__init__()

        # Иконка приложения.
        self.setWindowIcon(QtGui.QIcon("tangle.ico"))
        
        # Имя приложения.
        self.setWindowTitle("Tangle")

        # Отображение панели инструментов.
        self.addToolBar(ToolBar(self).CreateToolBar())

        # Создание объекта класса меню.
        self.menu = MenuBar(self)

        # Отображение меню.
        self.setMenuBar(self.menu.CreateMenuBar())

        # Фиксированный размер окна.
        self.setFixedSize(QSize(800, 600))
            
            
            


        

