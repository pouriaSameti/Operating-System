from multiprocessing import Process, Value, Array, Queue
from time import sleep
from lock import Lock


def add(num, value, id, lock: Lock):
    tmp = 0
    while True:
        while lock.acquire(id):
            print('add')
            num.value += value
            tmp = num.value
            sleep(2)
            lock.release(id)
        if tmp != num.value:
            print("Process conflict")


def sub(num, value, id, lock: Lock):
    tmp = 0
    while True:
        while lock.acquire(id):
            print('sub')
            num.value -= value
            tmp = num.value
            sleep(3)
            lock.release(id)
        if tmp != num.value:
            print("Process conflict")


def mul(num, value, id, lock: Lock):
    tmp = 0
    while True:
        while lock.acquire(id):
            print('mul')
            num.value *= value
            tmp = num.value
            sleep(4)
            lock.release(id)
        if tmp != num.value:
            print("Process conflict")


def div(num, value, id, lock: Lock):
    tmp = 0
    while True:
        while lock.acquire(id):
            print('div')
            num.value /= value
            tmp = num.value
            sleep(6)
            lock.release(id)
        if tmp != num.value:
            print("Process conflict")


def Show(num):
    while True:
        sleep(0.5)
        print(num.value)


if __name__ == '__main__':

    num = Value('d', 0.0)
    arr = Array('i', range(2))
    q = Queue()

    flags = [False, False, False, False]
    lock = Lock(flags)

    p1 = Process(target=add, args=(num, 10, 0, lock))
    p2 = Process(target=sub, args=(num, 5, 1, lock))
    p3 = Process(target=mul, args=(num, 2, 2, lock))
    p4 = Process(target=div, args=(num, 4, 3, lock))

    show = Process(target=Show, args=(num, ))
    show.start()

    sleep(1)
    p1.start()
    p2.start()
    p3.start()
    p4.start()

