""" 11000420: Moma """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([90, 100])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001748$
        # - You got something to say? 
        return None # TODO

    def __90(self, pick: int) -> int:
        # $script:0831180407001754$
        # - Are you sightseeing? Head north to the condominium complex. The staff is nice, and it's really pretty around there. Just sayin'.
        return -1

    def __100(self, pick: int) -> int:
        # $script:0831180407001755$
        # - $MyPCName$, do you like fish?
        if pick == 0:
            # $script:0831180407001756$
            # - Yep.
            return 101
        elif pick == 1:
            # $script:0831180407001757$
            # - Nope.
            return 102
        return -1

    def __101(self, pick: int) -> int:
        # $script:0831180407001758$
        # - Well $MyPCName$, you're more health-conscious than I thought. Fish is an excellent source of protein and other essential nutrients.
        return -1

    def __102(self, pick: int) -> int:
        # $script:0831180407001759$
        # - Oh, you should eat fish regularly. I thought you knew that, $MyPCName$. Do you only eat red meat? It's too fatty. Eating fish helps you lose weight.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (90, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (100, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (101, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (102, 0):
            return Option.CLOSE
        return Option.NONE
