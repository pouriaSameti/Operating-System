from multiprocessing import Value


class Lock:

    @classmethod
    def wait_producer_left(cls, left_producer: Value, right_producer: Value, turn_produce: Value):
        turn_produce.value = 1  # 1 -> right     0-> left
        left_producer.value = 1
        while right_producer.value == 1 and turn_produce.value == 1:
            pass

