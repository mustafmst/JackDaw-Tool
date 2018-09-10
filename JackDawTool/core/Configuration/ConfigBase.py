class ConfigBase:
    def __init__(self):
        self.zookeeper = ""
        self.brokers = ""

    def __str__(self):
        return '{};{}'.format(self.zookeeper,
                              self.brokers)

    def set_zookeeper(self, conf):
        self.zookeeper = conf

    def set_brokers(self, conf):
        self.brokers = conf
