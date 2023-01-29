from registers import *
from process import Process
import numpy as np


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
    def store_operate(cls, value: float, temp: Temp, acc: Accumulator):
        temp.set(value)
        acc.set(value)

    @classmethod
    def arithmetic_operate(cls, value: float, operation: str, temp: Temp, acc: Accumulator):
        if operation not in cls.__arithmetic:
            raise Exception("This is not arithmetic operation")

        temp.set(value)

        result = 0.0
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

    def is_exist_process(self, process_id):
        return process_id in self.__processes.keys()

    def give_process(self, p_id: str):
        return self.__processes[p_id]

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
    def run(cls, os, pc: PC, ir: IR, acc: Accumulator, temp: Temp):
        counter = 0
        for command in OS.read_commands():
            print('loop:', counter)
            print(command)
            counter += 1

            if 'create_process' in command:
                signal, process_id, file_name = command.split()
                instructions = OS.read_instructions(file_name)
                process = Process(process_id, instructions, os)
                process.run(signal, os, pc, ir, acc, temp)

            else:
                signal, process_id = command.split()
                if os.is_exist_process(process_id):
                    process = os.give_process(process_id)
                    process.run(signal, os, pc, ir, acc, temp)
                else:
                    print("Process Does Not Exist")

    @classmethod
    def read_commands(cls):
        address = 'input commands\\' + 'commands' + '.txt'
        return np.loadtxt(address, dtype='str', delimiter="\n")

    @classmethod
    def read_instructions(cls, file_name: str):
        address = 'input commands\\' + file_name
        return np.loadtxt(address, dtype='str', delimiter="\n")

    @property
    def ram(self):
        return self.__ram
