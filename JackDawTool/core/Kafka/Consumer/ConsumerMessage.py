import datetime

from pip._vendor import msgpack


class ConsumerMessage:
    def __init__(self, consumerRecord):
        self._partition = consumerRecord.partition
        self._offset = consumerRecord.offset
        self._value = consumerRecord.value.decode('utf-8')

    def __str__(self):
        return '[partition: {}; offset: {}] {}'.format(self._partition, self._offset, self._value)
