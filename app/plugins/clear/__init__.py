import sys
from app.commands import Command
from app.history import History
import logging


class ClearCommand(Command):
    def execute(self):
        hist_inst = History()
        hist_inst.clear()
        print('History has been cleared!')
        logging.info('Calculator history has been cleared')
