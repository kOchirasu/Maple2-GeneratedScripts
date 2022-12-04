""" 11000134: Wolf Heart """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000557$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000558$
        # - Once a year, the Murpagoth warriors go on a pilgrimage through the Vayar Mountains. By the time they return, they've grown much stronger than they were before.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
