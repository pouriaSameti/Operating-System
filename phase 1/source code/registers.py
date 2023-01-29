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


class Accumulator:

    def __init__(self):
        self.__value = [-sys.maxsize]

    def reset(self):
        self.__value[0] = -sys.maxsize

    def is_empty(self):
        return -sys.maxsize == self.__value[0]

    def set_to_temp(self, temp: Temp):
        if temp.is_empty():
            raise Exception("Temp Register is Null.We can't Write into Accumulator")

        self.__value[0] = temp.get()

    def set(self, value):
        self.__value[0] = value

    def get(self):
        if self.is_empty():
            raise Exception("Accumulator Register is Empty")

        return self.__value[0]

