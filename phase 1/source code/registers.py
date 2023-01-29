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

    def __str__(self):
        return f"temp: {self.get()}"


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

    def __str__(self):
        return f"accumulator: {self.get()}"


class PC:

    def __init__(self):
        self.__counter = 0

    def increment(self):
        self.__counter += 1

    def set(self, value: int):
        self.__counter = value

    def reset(self):
        self.__counter = 0

    def get(self):
        return self.__counter

    def __str__(self):
        return f"pc: {self.get()}"


class IR:

    def __init__(self):
        self.__instruction = ''
        self.__immediate = -sys.maxsize

    def is_empty(self):
        return self.__instruction == '' and self.__immediate == -sys.maxsize

    def set(self, instruction: str, immediate: int):
        IR.__check_instruction(instruction)
        self.__instruction = instruction
        self.__immediate = immediate

    def reset(self):
        self.__instruction = ''
        self.__immediate = -sys.maxsize

    def get_instruction(self):
        return self.__instruction

    def get_immediate(self):
        return self.__immediate

    @classmethod
    def __check_instruction(cls, instruction: str):
        ir_arr = ['load', 'add', 'sub', 'mul']

        if instruction not in ir_arr:
            raise Exception("Invalid Instruction")