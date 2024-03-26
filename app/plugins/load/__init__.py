import sys
from app.commands import Command
from app.history import History
import logging


class LoadCommand(Command):
    def execute(self):
        his_instance = History()
        calc_data = his_instance.get_as_data_frame().to_string(index=False)
        print('Calculator history data:\n', calc_data)
        logging.info('Calculator history has been fetched and loaded: %s', calc_data)
