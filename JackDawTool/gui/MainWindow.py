from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem

from JackDawTool.gui.MainWindowLayout import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self._topics = dict()
        self._window = QMainWindow()
        self._window_layout = Ui_MainWindow()
        self._window_layout.setupUi(self._window)
        self._window.show()

    def add_connect_click_event(self, event):
        self._window_layout \
            .buttonConnect \
            .clicked \
            .connect(lambda _:
                     event(
                         self._window_layout.lineEditZookeeper.text(),
                         self._window_layout.lineEditBrokers.text()
                     ))
        # new_message_signal.connect(self.write_to_text_area)

    def write_to_text_area(self, topic, msg):
        self._window_layout.messages.append(msg)

    def add_topics(self, topics):
        for topic in topics:
            topic_item = QTreeWidgetItem(self._window_layout.treeWidget)
            topic_item.setText(0, topic)
            self._topics[topic] = topic_item
        pass
