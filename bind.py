from PyQt5.QtWidgets import QMainWindow

from ui.mainwindow import Ui_mainWindow
from src.shortcut import Shortcut


def bind(mainwindow: QMainWindow, ui_mainwindow: Ui_mainWindow):
    shortcut = Shortcut(mainwindow)

    ui_mainwindow.toolButton_Exec.clicked.connect(lambda : shortcut.chooseExecFile(ui_mainwindow.lineEdit_Exec))
    ui_mainwindow.toolButton_Icon.clicked.connect(lambda : shortcut.chooseIcon(ui_mainwindow.lineEdit_Icon))
    ui_mainwindow.pushButton_Create.clicked.connect(
        lambda : shortcut.createShortCut(
            ui_mainwindow.lineEdit_Name,
            ui_mainwindow.lineEdit_Exec,
            ui_mainwindow.lineEdit_Icon,
            ui_mainwindow.lineEdit_Command
        )
    )