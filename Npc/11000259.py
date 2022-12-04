""" 11000259: Dark Wind Agent """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001069$
        # - What seems to be the problem?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407001070$
        # - I'd keep a low profile if I were you.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407001071$
        # - It's going to be tough, but we have to comb through the records for clues. We can't let them catch us off guard again.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
