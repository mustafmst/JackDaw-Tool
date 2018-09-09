import sys

from PyQt5.QtWidgets import QApplication

from JackDawTool.core.Configuration.ConfigFactory import ConfigFactory
from JackDawTool.core.Kafka.Consumer.ConsumersPool import ConsumersPool
from JackDawTool.gui.MainWindow import MainWindow


class JackDawApp:
    def __init__(self):
        self._consumers_pool = ConsumersPool()
        self._qt_app = QApplication(sys.argv)
        self._main_window = MainWindow()
        self._config = ConfigFactory.create()
        self.create_main_window()
        sys.exit(self._qt_app.exec_())

    def create_main_window(self):
        self._main_window.add_connect_click_event(self.connectAction,
                                                  self._consumers_pool.new_message)

    def connectAction(self, zookeeper, brokers, topic):
        print("Connecting...")
        self._config.set_zookeeper(zookeeper)
        self._config.set_brokers(brokers)
        self._config.set_topic(topic)
        print(self._config)
        self._consumers_pool.create_consumer(self._config.brokers, self._config.topic)
