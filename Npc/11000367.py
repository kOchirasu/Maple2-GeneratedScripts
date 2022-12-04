""" 11000367: Skittle """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001514$
        # - What is it, meow?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001516$
        # - Do you believe in love at first sight, meow? I do! Look at the cat next to me. Isn't she beautiful? Me-ow!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
