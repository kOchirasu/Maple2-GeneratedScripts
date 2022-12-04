""" 11003960: Wizard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614143707010011$
        # - They have so many tasty foods here!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614143707010012$
        # - Hey... Do you have more Orange Mushroom cookies...? I ate all of mine, hehe.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
