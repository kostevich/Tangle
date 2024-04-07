#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction
from MainWindow.EventHandler import EventHandler

#==========================================================================================#
# >>>>> ГЛАВНОЕ ОКНО <<<<< #
#==========================================================================================#

class MenuBar():

    #==========================================================================================#
    # >>>>> КОНСТРУКТОР ПАНЕЛИ МЕНЮ <<<<< #
    #==========================================================================================#

    def __init__(self, window):

        # Создание меню.
        self.MenuBarObject = QMenuBar()

        # Передаём данные класса MainWindow.
        self.window = window

    #==========================================================================================#
    # >>>>> СОЗДАНИЕ ПАНЕЛИ МЕНЮ <<<<< #
    #==========================================================================================#

    def CreateMenuBar(self):
    
        # Создание кнопок меню.
        Main = QMenu("Main", self.window)
        Info = QMenu("Info", self.window)

        # Добавление кнопок на панель меню.
        self.MenuBarObject.addMenu(Main)
        self.MenuBarObject.addMenu(Info)

        # Создание кнопок подменю.
        self.FromGitHub = QAction("Add local repository", self.window)
        self.ToGitHub = QAction("Clone repository", self.window)
        self.NewRepository = QAction("Create new repository", self.window)
        self.AboutProgram = QAction("About program", self.window)

        # Добавление кнопок подменю в меню.
        Main.addAction(self.FromGitHub)
        Main.addAction(self.ToGitHub)
        Main.addAction(self.NewRepository)
        Info.addAction(self.AboutProgram)

        # Обработка нажатия кнопки.
        self.EventHandlerObject = EventHandler(self.window)
        self.AboutProgram.triggered.connect(self.EventHandlerObject.ClickAboutProgram)

        return self.MenuBarObject
            