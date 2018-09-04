import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from JackDawTool.core.Configuration.ConfigFactory import ConfigFactory
from JackDawTool.core.Kafka.Consumer.Consumer import Consumer

from JackDawTool.gui.MainWindow import Ui_MainWindow


class JackDawApp:
    def __init__(self):
        self.qt_app = QApplication(sys.argv)
        self.main_window = Ui_MainWindow(QMainWindow())
        self.config = ConfigFactory.create()
        self.create_main_window()
        sys.exit(self.qt_app.exec_())

    def create_main_window(self):
        self.main_window.setupUi()
        self.main_window.setActions(self.connectAction)

    def connectAction(self, zookeeper, brokers, topic):
        print("Connecting...")
        self.config.set_zookeeper(zookeeper)
        self.config.set_brokers(brokers)
        self.config.set_topic(topic)
        self.main_window.write_message(str(self.config))
        self._consumer = Consumer(self.config.topic)
        self._consumer.read(self.main_window.write_message)

