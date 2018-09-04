from kafka import KafkaConsumer


class Consumer:
    def __init__(self, topic):
        self._consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
        self._consumer.subscribe([topic])

    def read(self, writer):
        for msg in self._consumer:
            writer(str(msg.value))
            print(msg.value)
