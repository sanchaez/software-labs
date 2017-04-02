from model import Model
from view import View


class Controller:

    def __init__(self):
        self.__interface = View()
        self.__scheduler = Model()

    def run(self):
        pass

    def edit_event(self):
        pass

    def delete_event(self):
        pass

    def add_event(self):
        pass

    def show_event(self):
        pass