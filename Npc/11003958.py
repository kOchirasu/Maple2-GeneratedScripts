""" 11003958: Assassin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614143707010007$
        # - ...What business do you have with me?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614143707010008$
        # - ...You seem strong.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
