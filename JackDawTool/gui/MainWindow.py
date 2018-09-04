from PyQt5.QtWidgets import QMainWindow

from JackDawTool.gui.MainWindowLayout import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self._window = QMainWindow()
        self._window_layout = Ui_MainWindow()
        self._window_layout.setupUi(self._window)
        self._window.show()

    def add_connect_click_event(self, event):
        self._window_layout \
            .buttoneConnect \
            .clicked \
            .connect(lambda _:
                     event(
                         self._window_layout.lineEditZookeeper.text(),
                         self._window_layout.lineEditBrokers.text(),
                         self._window_layout.lineEditTopic.text()
                     ))

    def write_to_text_area(self, msg):
        self._window_layout.messages.append(msg)
