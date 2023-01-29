from registers import *


class OS:

    __store = ["load"]
    __arithmetic = ['add', 'sub', 'mul']
    __signals = ['create_process', 'run_process', 'block_process', 'unblock_process', 'show_context', 'kill_process']

    def __init__(self):
        self.__ram = {}  # key: 'process_id + line_number'  &  value: command
        self.__processes = {}  # key: 'process_id  &  value: process object

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

    def add_process(self, process):
        self.__processes[process.get_id()] = process

    def send_to_ram(self, process):
        counter = 0
        for cmd in process.get_commands():
            self.__ram[f"{process.get_id()} {counter}"] = cmd
            counter += 1

    def kill_process(self, process_id):
        self.__processes.pop(process_id)

    @classmethod
    def reset_registers(cls, ir: IR, acc: Accumulator, temp: Temp):
        ir.reset()
        acc.reset()
        temp.reset()

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
