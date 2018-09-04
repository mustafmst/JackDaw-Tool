import sys

from PyQt5.QtWidgets import QApplication

from JackDawTool.core.Configuration.ConfigFactory import ConfigFactory
from JackDawTool.gui.MainWindow import MainWindow


class JackDawApp:
    def __init__(self):
        self._qt_app = QApplication(sys.argv)
        self._main_window = MainWindow()
        self._config = ConfigFactory.create()
        self.create_main_window()
        sys.exit(self._qt_app.exec_())

    def create_main_window(self):
        self._main_window.add_connect_click_event(self.connectAction)

    def connectAction(self, zookeeper, brokers, topic):
        print("Connecting...")
        self._config.set_zookeeper(zookeeper)
        self._config.set_brokers(brokers)
        self._config.set_topic(topic)
        print(self._config)
        self._main_window.write_to_text_area(str(self._config))
        # self._consumer = Consumer(self.config.topic)
        # thr = threading.Thread(target=self._consumer.read, args=(self.main_window.write_message,))
        # thr.start()
