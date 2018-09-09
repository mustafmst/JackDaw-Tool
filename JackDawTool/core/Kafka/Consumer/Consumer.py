import time

from kafka import KafkaConsumer


class Consumer:
    def __init__(self, topic):
        self._consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
        self._consumer.subscribe([topic])
        self._topic = topic

    def read(self, signal):
        for msg in self._consumer:
            signal.emit(self._topic, str(msg))
            print(msg.value)
            time.sleep(2)
