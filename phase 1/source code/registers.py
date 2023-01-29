import sys


class Temp:

    def __init__(self):
        self.__value = [-sys.maxsize]

    def is_empty(self):
        return -sys.maxsize == self.__value[0]

    def set(self, amount: int):
        self.__value[0] = amount

    def get(self):
        if self.is_empty():
            raise Exception("Temp Register is Empty")
        return self.__value[0]

    def reset(self):
        self.__value[0] = -sys.maxsize


