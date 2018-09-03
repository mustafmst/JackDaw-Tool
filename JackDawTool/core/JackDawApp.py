import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from JackDawTool.core.Config import Config
from JackDawTool.gui.MainWindow import Ui_MainWindow


class JackDawApp:
    def __init__(self):
        self.config = Config()
        qt_app = QApplication(sys.argv)
        w = QMainWindow()
        main_window = Ui_MainWindow()
        main_window.setupUi(w)
        main_window.setActions(self.connectAction)
        w.show()
        sys.exit(qt_app.exec_())

    @staticmethod
    def connectAction():
        print("Connecting...")
