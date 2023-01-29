from registers import *


class OS:

    __store = ["load"]
    __arithmetic = ['add', 'sub', 'mul']

    @classmethod
    def type_instruction(cls, ins: str):
        if ins in cls.__store:
            return 'store'

        if ins in cls.__arithmetic:
            return 'arithmetic'

        else:
            return '-'

    @classmethod
    def store_operate(cls, instruction: str, value: int, ir: IR, temp: Temp, acc: Accumulator):
        ir.set(instruction, value)
        temp.set(value)
        acc.set(value)

