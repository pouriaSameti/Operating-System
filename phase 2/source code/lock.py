import sys


class Queue:

    def __init__(self, size):
        self.__array = [0 for _ in range(size)]
        self.__size = size
        self.__front = 0
        self.__rear = 0
        self.__count = 0



