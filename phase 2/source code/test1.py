from multiprocessing import Process, Value, Array, Queue, Lock
from time import sleep


def add(num, value, lock: Lock):
    tmp = 0
    while True:
        lock.acquire()
        print('add')
        num.value += value
        tmp = num.value
        sleep(1)
        lock.release()
        if tmp != num.value:
            print("Process conflict")


def sub(num, value, lock: Lock):
    tmp = 0
    while True:
        lock.acquire()
        print('sub')
        num.value += value
        tmp = num.value
        sleep(1.5)
        lock.release()
        if tmp != num.value:
            print("Process conflict")


def mul(num, value, lock: Lock):
    tmp = 0
    while True:
        lock.acquire()
        print('mul')
        num.value *= value
        tmp = num.value
        sleep(2)
        lock.release()
        if tmp != num.value:
            print("Process conflict")


def div(num, value, lock: Lock):
    tmp = 0
    while True:
        lock.acquire()
        print('div')
        num.value /= value
        tmp = num.value
        sleep(3)
        lock.release()
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
    lock = Lock()

    p1 = Process(target=add, args=(num, 10, lock))
    p2 = Process(target=sub, args=(num, 5, lock))
    p3 = Process(target=mul, args=(num, 2, lock))
    p4 = Process(target=div, args=(num, 4, lock))

    show = Process(target=Show, args=(num,))
    show.start()
    sleep(1)
    p1.start()
    p2.start()
    p3.start()
    p4.start()


