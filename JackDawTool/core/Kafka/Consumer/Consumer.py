from kafka import KafkaConsumer

from JackDawTool.core.Kafka.Consumer.ConsumerMessage import ConsumerMessage


class Consumer:
    def __init__(self, brokers, topic):
        self._consumer = KafkaConsumer(bootstrap_servers=brokers)
        self._consumer.subscribe([topic])
        self._topic = topic

    def read(self, signal):
        for record in self._consumer:
            msg = ConsumerMessage(record)
            signal.emit(self._topic, str(msg))
            print(msg)
