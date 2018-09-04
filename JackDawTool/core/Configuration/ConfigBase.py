class ConfigBase:
    def __init__(self):
        self.zookeeper = ""
        self.brokers = ""
        self.topic = ""

    def __str__(self):
        return str(self.zookeeper + ";" + self.brokers + ";" + self.topic)

    def set_zookeeper(self, conf):
        self.zookeeper = conf

    def set_brokers(self, conf):
        self.brokers = conf

    def set_topic(self, conf):
        self.topic = conf
