#!/usr/bin/python

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QListWidget, QVBoxLayout, QHBoxLayout

from PyQt6.QtGui import QAction

ListRepository = ("1", "2", "3", "4", "5",)
FunctionRepository = ("уДАИЛАСМВ", "2", )
# Создание приложения.
Tangle = QApplication([])

# Создание интерфейса приложения на основе класса QMainWindow.
class MainWindow(QMainWindow):
    # Конструирование интерфейса приложения.
    def __init__(self):
        super(MainWindow, self).__init__()
        # Имя приложения.
        self.setWindowTitle("Tangle")
        

        # Создание названия окошка.
        Lable = QLabel("Repository", self)
        # Перемещение окошка.
        Lable.move(150, 100)


        # Создание списка репозиториев.
        self.List = QListWidget(self)
        # Перемещение.
        self.List.move(50, 150)
        # Размер списка.
        self.List.setFixedSize(300, 500)
        # Добавление элементов списка.
        self.List.addItems(ListRepository)

        self.List.itemClicked.connect(self.ChoiceRepository)
    

        # Создание списка функций для работы репозитория.
        self.FunctionsRepository = QListWidget(self)
        # Перемещение.
        self.FunctionsRepository.move(450, 450)
        # Размер списка.
        self.FunctionsRepository.setFixedSize(100, 100)
        # Добавление элементов списка.
        self.FunctionsRepository.addItems(FunctionRepository)

        self.FunctionsRepository.itemClicked.connect(self.ChoiceRepository)
        

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
        




        def ChoiceRepository(self, item):
                print("Вы кликнули: {}".format(item.text()))
                if item.text()=="item2": print("Делайте что-нибудь.")

# Создание окошка.
window = MainWindow()
# Отображение окошка.
window.show()

# Обработка событий происходящих в окошке.
Tangle.exec()