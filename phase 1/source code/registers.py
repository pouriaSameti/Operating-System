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


class PC:

    def __init__(self):
        self.__amount = 0
        self.__ra = 0  # ra == return address

    def increment(self):
        self.__amount += 1

    def reset(self):
        self.__amount = 0

    def get(self):
        return self.__amount

    def get_ra(self):
        return self.__ra

    def jump(self, new_address: int):
        self.__ra = self.__amount
        self.__amount = new_address

    def jump_back(self):
        self.__amount = self.__ra
        self.__ra = 0


class IR:

    def __init__(self, instruction: str, immediate: int):
        IR.__check_instruction(instruction)
        self.__instruction = instruction
        self.__immediate = immediate

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