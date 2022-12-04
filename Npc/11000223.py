""" 11000223: Morris """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000973$
        # - Are you here to talk to me? But why?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000975$
        # - I don't understand women. It feels like they're always changing their minds. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
