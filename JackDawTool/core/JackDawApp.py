import sys

from PyQt5.QtWidgets import QApplication

from JackDawTool.core.Configuration.ConfigFactory import ConfigFactory
from JackDawTool.core.Kafka.KafkaConnection import KafkaConnection
from JackDawTool.gui.MainWindow import MainWindow


class JackDawApp:
    kafka_connection = None

    def __init__(self):
        self._qt_app = QApplication(sys.argv)
        self._main_window = MainWindow()
        self._config = ConfigFactory.create()
        self.add_connect_action()
        sys.exit(self._qt_app.exec_())

    def add_connect_action(self):
        self._main_window.add_connect_click_event(self.connect_action)

    def connect_action(self, zookeeper, brokers):
        print("Connecting...")
        self._config.set_zookeeper(zookeeper)
        self._config.set_brokers(brokers)
        self.kafka_connection = KafkaConnection(self._config)
        self.kafka_connection.get_topics()
        # self.kafka_connection.consumers_pool.create_consumer(self._config.brokers, self._config.topic)
