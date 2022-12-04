""" 11000547: Eka """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002320$
        # - Ugh... 
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002322$
        # - Checkpoint... under attack... $map:02000076$... in danger...
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407002323$
        # - I-I'm okay... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
