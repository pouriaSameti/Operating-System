from multiprocessing import Process, Queue, Value
import RightSide
import LeftSide
from lock import Lock


def main():

    street = Value('d', 0)
    id = Value('d', 1)

    turn_produce = Value('d', 0)
    turn_consume = Value('d', 0)

    left_produce = Value('d', 0)
    right_produce = Value('d', 0)

    left_consume = Value('d', 0)
    right_consume = Value('d', 0)
    lock = Lock()

    car_list1 = Queue(maxsize=10)
    car_list2 = Queue(maxsize=10)

    prod1 = Process(target=RightSide.producer, args=(car_list1, id, left_produce, right_produce, turn_produce, lock))
    cons1 = Process(target=RightSide.consumer, args=(car_list1, street, left_consume, right_consume, turn_consume, lock))
    prod1.start()
    cons1.start()

    prod2 = Process(target=LeftSide.producer, args=(car_list2, id, left_produce, right_produce, turn_produce, lock))
    cons2 = Process(target=LeftSide.consumer, args=(car_list2, street, left_consume, right_consume, turn_consume, lock))
    prod2.start()
    cons2.start()


if __name__ == '__main__':
    main()

