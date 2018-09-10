import time

from kafka import KafkaConsumer

from JackDawTool.core.Kafka.Consumer.ConsumersPool import ConsumersPool


class KafkaConnection:
    def __init__(self, config):
        self._zookeeper = config.zookeeper
        self._brokers = config.brokers
        self.consumers_pool = ConsumersPool()
        self._data_consumer = KafkaConsumer(group_id=str(time.time()), bootstrap_servers=[config.brokers])
        pass

    def get_topics(self):
        topics = self._data_consumer.topics()
        return topics
