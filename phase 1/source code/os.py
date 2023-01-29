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
    def store_operate(cls, value: int, temp: Temp, acc: Accumulator):
        temp.set(value)
        acc.set(value)

    @classmethod
    def arithmetic_operate(cls, value: int, operation: str, temp: Temp, acc: Accumulator):
        if operation not in cls.__arithmetic:
            raise Exception("This is not arithmetic operation")

        temp.set(value)

        result = 0
        match operation:
            case 'add':
                result = acc.get() + temp.get()
            case 'sub':
                result = acc.get() - temp.get()
            case 'mul':
                result = acc.get() * temp.get()

        acc.set(result)

    @classmethod
    def run(cls, commands: list, os, ir: IR, temp: Temp, acc: Accumulator, pc: PC):
        for cmd in commands:
            pc.increment()
            instruction, value = cmd.split()
            ir.set(instruction, int(value))
            if os.type_instruction(instruction) == 'store':
                os.store_operate(int(value), temp, acc)

            if os.type_instruction(instruction) == 'arithmetic':
                os.arithmetic_operate(int(value), instruction, temp, acc)

        pc.reset()
