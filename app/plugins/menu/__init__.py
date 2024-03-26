import sys
from app.commands import Command

class MenuCommand(Command):
    def __init__(self, handler):
        self.handler = handler

    def execute(self):
        menu_list = self.handler.menu_list()
        print("The Menu options are:", list(menu_list))

