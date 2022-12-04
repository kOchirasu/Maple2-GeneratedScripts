""" 11000409: Julian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001728$
        # - Welcome, $MyPCName$!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407001729$
        # - The forest trail is too dangerous. We have to make it safe again, as soon as possible.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407001730$
        # - $npcName:99000041$ are making this trail too dangerous to travel.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
