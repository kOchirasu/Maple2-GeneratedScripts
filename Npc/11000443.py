""" 11000443: Cathy Mart Employee """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001863$
        # - Can I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001865$
        # - If we don't get that money back, it's coming out of <i>my</i> paycheck...
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407001866$
        # - I don't know who's worse, the boss or the robbers.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
