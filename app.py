from bind import bind
from ui.mainwindow import Ui_mainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainwindow = QMainWindow()
    ui_components = Ui_mainWindow()
    ui_components.setupUi(mainwindow)
    mainwindow.show()

    bind(mainwindow, ui_components)

    sys.exit(app.exec_())