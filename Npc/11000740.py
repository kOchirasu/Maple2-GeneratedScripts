""" 11000740: Pia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002877$
        # - Hm...
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002881$
            # - Err? Are you a traveler? You look... cool. 
            return 40
        elif self.index == 1:
            # $script:0831180407002882$
            # - I'm cooler, though. Hee hee!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
