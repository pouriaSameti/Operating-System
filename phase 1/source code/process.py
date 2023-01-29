from registers import *
from os import OS


class Process:
    __states = ['ready', 'running', 'blocked']

    def __init__(self, p_id: str, commands: list, os: OS):
        self.__process_id = p_id
        self.__context = {'ir': ('', -sys.maxsize), 'acc': -sys.maxsize, 'temp': -sys.maxsize,
                          'current_line': -sys.maxsize}
        self.__state = '-'
        self.__commands = commands

        self.__start_line = len(os.ram)
        self.__end_pc = self.__start_line + len(commands)
        self.__current_line = 0

    def get_id(self):
        return self.__process_id

    def get_commands(self):
        return self.__commands

    def run(self, signal: str, os: OS, pc: PC, ir: IR, acc: Accumulator, temp: Temp):

        if signal == 'create_process':
            self.__state = Process.__states[0]
            os.add_process(self)
            os.send_to_ram(self)

        if signal == 'run_process' and self.__state != Process.__states[2]:
            self.__state = Process.__states[1]

            pc.set(self.__current_line + self.__start_line)

            instruction, value = os.ram[f'{self.__process_id} {self.__current_line}'].split()
            ir.set(instruction, int(value))

            acc.set(self.__context['acc'])

            if os.type_instruction(instruction) == 'store':
                os.store_operate(int(value), temp, acc)

            if os.type_instruction(instruction) == 'arithmetic':
                os.arithmetic_operate(int(value), instruction, temp, acc)

            self.__current_line += 1