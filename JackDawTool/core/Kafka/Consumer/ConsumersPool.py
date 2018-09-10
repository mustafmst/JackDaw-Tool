from threading import Thread

from PyQt5.QtCore import QObject, pyqtSignal

from JackDawTool.core.Kafka.Consumer.Consumer import Consumer


class ConsumersPool(QObject):
    new_message = pyqtSignal(str, str)

    def __init__(self):
        super(ConsumersPool, self).__init__()
        self._consumers = {}

    def create_consumer(self, brokers, topic):
        consumer = Consumer(brokers, topic)
        tr = Thread(target=consumer.read, args=(self.new_message,))
        self._consumers[topic] = tr
        tr.setDaemon(True)
        tr.start()

