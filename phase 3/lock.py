from multiprocessing import Value


class Lock:

    @classmethod
    def wait_producer_left(cls, left_producer: Value, right_producer: Value, turn_produce: Value):
        turn_produce.value = 1  # 1 -> right     0-> left
        left_producer.value = 1
        while right_producer.value == 1 and turn_produce.value == 1:
            pass

    @classmethod
    def wait_producer_right(cls, left_producer: Value, right_producer: Value, turn_produce: Value):
        turn_produce.value = 0
        right_producer.value = 1
        while left_producer.value == 1 and turn_produce.value == 0:
            pass

    @classmethod
    def wait_consumer_left(cls, left_consume, right_consumer, turn_consumer):
        left_consume.value = 1
        turn_consumer.value = 1
        while right_consumer.value == 1 and turn_consumer.value == 1:
            pass

    @classmethod
    def signal(cls, val: Value):
        val.value = 0
