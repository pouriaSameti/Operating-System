import sys


class Temp:

    def __init__(self):
        self.__value = [-sys.maxsize]

    def is_empty(self):
        return -sys.maxsize == self.__value[0]

    def set(self, amount: int):
        self.__value[0] = amount

    def reset(self):
        self.__value[0] = -sys.maxsize




