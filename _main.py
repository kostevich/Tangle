#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods import CheckPythonMinimalVersion
from PyQt6.QtWidgets import QApplication
from MainWindow.MWindow import MainWindow

#==========================================================================================#
# >>>>> ИНИЦИАЛИЗАЦИЯ СКРИПТА <<<<< #
#==========================================================================================#

# Проверка поддержки используемой версии Python.
CheckPythonMinimalVersion(3, 10)

#==========================================================================================#
# >>>>> СОЗДАНИЕ ПРИЛОЖЕНИЯ <<<<< #
#==========================================================================================#

# Создание приложения.
Tangle = QApplication([])

#==========================================================================================#
# >>>>> НАСТРОЙКА ПРИЛОЖЕНИЯ <<<<< #
#==========================================================================================#

# Стиль приложения.
Tangle.setStyle("Fusion")

# Создание окошка.
window = MainWindow()

# Отображение окошка.
window.show()

#==========================================================================================#
# >>>>> ОБРАБОТКА СОБЫТИЙ ПРИЛОЖЕНИЯ <<<<< #
#==========================================================================================#

# Обработка событий происходящих в окошке.
Tangle.exec()