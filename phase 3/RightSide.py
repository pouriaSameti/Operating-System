from multiprocessing import Process, Queue, Value, Array
from time import sleep
from Car import Car
from lock import Lock


def producer(queue, id, left_produce, right_produce, turn_producer, lock: Lock):
    print('Producer: Running', flush=True)
    while True:
        value = Car(id.value)
        lock.wait_producer_right(left_produce, right_produce, turn_producer)
        id.value += 1
        lock.signal(right_produce)
        sleep(100)
        queue.put(value)


def consumer(queue, street):
    print('Consumer: Running', flush=True)
    while True:
        item = queue.get()
        street.value = item.id
        print('car id: ', item.id, 'sleep: ', item.time)
        temp = street.value
        sleep(item.time)
        if temp != street.value:
            print('Process conflict!')