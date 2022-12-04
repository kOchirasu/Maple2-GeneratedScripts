""" 11000100: Dede """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000393$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000395$
        # - Can't touch this! Na na na... Um, is that one still popular?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
