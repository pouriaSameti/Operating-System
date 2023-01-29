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