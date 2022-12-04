""" 11003522: Little Tree Sprite """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115009026$
        # - What's happening?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115009027$
        # - Lookit me!
        return -1

    def __40(self, pick: int) -> int:
        # $script:0816160115009028$
        # - What's happening?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
