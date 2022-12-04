""" 11000328: Merjafar """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001333$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001335$
            # - People nowadays tend to throw their things away the moment they're done with them. It's a shame, really. 
            return 30
        elif self.index == 1:
            # $script:0831180407001336$
            # - Antique items are precious relics of the past. You can trade antiques, but you can't bring the past back.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
