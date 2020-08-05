import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow

DESKTOP_ENTRY_PATH = os.path.expanduser("~") + "/.local/share/applications"
DESKTOP_ENTRY_CONTENT = "[Desktop Entry]\n"

class Shortcut:

    def __init__(self, MainWindow: QMainWindow):
        self.mainwindow = MainWindow

        self.name = ''
        self.exec = ''
        self.icon = ''
        self.command = ''

    def chooseExecFile(self, lineEdit: QtWidgets.QLineEdit):
        file = QFileDialog.getOpenFileName(
            self.mainwindow,
            "Choose execute file",
            os.path.expanduser("~"),
            "All files(*.*);;Appimage(*.appimage)"
        )
        lineEdit.setText(file[0])
        self.exec = file[0]

    def chooseIcon(self, lineEdit: QtWidgets.QLineEdit):
        file = QFileDialog.getOpenFileName(
            self.mainwindow,
            "Choose execute file",
            os.path.expanduser("~"),
            "Image(*.png);;All files(*.*)"
        )
        lineEdit.setText(file[0])
        self.icon = file[0]

    def createShortCut(
            self,
            nameEdit: QtWidgets.QLineEdit,
            execEdit: QtWidgets.QLineEdit,
            iconEdit: QtWidgets.QLineEdit,
            commandEdit: QtWidgets.QLineEdit
    ):
        name = self.__getNameText(nameEdit)
        if not name:
            return

        exec = self.__getExecText(execEdit)
        if not exec:
            return

        icon = self.__getIconText(iconEdit)
        if not icon:
            return

        command = self.__getCommandText(commandEdit)

        self.name = name
        self.exec = exec
        self.icon = icon
        self.command = " " + command

        self.__prepareContent()
        self.__createShortCut()

    def __getLineEditText(self, lineEdit: QtWidgets.QLineEdit, title: str = "", content: str = "", isNull: bool = False):
        text = lineEdit.text()
        if not isNull and len(text) == 0:
            QMessageBox.warning(self.mainwindow, title, content, QMessageBox.Yes, QMessageBox.Yes)
            return None
        return text

    def __getNameText(self, nameEdit: QtWidgets.QLineEdit):
        return self.__getLineEditText(nameEdit, "No Name", "Please input name")

    def __getExecText(self, execEdit: QtWidgets.QLineEdit):
        exec = self.__getLineEditText(execEdit, "No exec", "Please choose exec")
        if not exec:
            return None

        if not os.path.exists(exec):
            QMessageBox.warning(self.mainwindow, "Error!", "Exec file is not exists", QMessageBox.Ok, QMessageBox.Ok)
            return None
        return exec

    def __getIconText(self, iconEdit: QtWidgets.QLineEdit):
        icon = self.__getLineEditText(iconEdit, "No Name", "Please choose icon")
        if not icon:
            return None

        if not os.path.exists(icon):
            QMessageBox.warning(self.mainwindow, "Error!", "Icon file is not exists", QMessageBox.Ok, QMessageBox.Ok)
            return None
        return icon

    def __getCommandText(self, commandEdit: QtWidgets.QLineEdit):
        return self.__getLineEditText(commandEdit, isNull=True)

    def __prepareContent(self):
        content = DESKTOP_ENTRY_CONTENT
        content = content + "Name=" + self.name + "\n"
        content = content + "Exec=" + self.exec + self.command + "\n"
        content = content + "Icon=" + self.icon + "\n"
        content = content + "Type=Application\n"
        content = content + "Terminal=false\n"
        self.content = content

    def __createShortCut(self):
        if not self.name:
            return None

        file = DESKTOP_ENTRY_PATH + "/" + self.name + ".desktop"
        if os.path.exists(file):
            msg = QMessageBox.warning(self.mainwindow, "Warning", "Shortcut icon is already exist! This will override it!", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if msg != QMessageBox.Yes:
                return None

        try:
            with open(file, "w", encoding='utf-8') as f:
                f.write(self.content)
            QMessageBox.information(self.mainwindow, "Success!", self.name + " create success!", QMessageBox.Yes, QMessageBox.Yes)
        except Exception as e:
            QMessageBox.warning(self.mainwindow, "Error!", str(e), QMessageBox.Yes, QMessageBox.Yes)
            return None