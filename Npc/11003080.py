""" 11003080: Columbo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0113143107007757$
        # - Ahhh, I want to get better soon so I can go on adventures again!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0113143107007760$
        # - How soon until I can sail again? Cough, cough! I want to be well so I can set off to find the wonders of the world.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0113143107007761$
        # - $MyPCName$, thank you for telling me about your adventures! I hope I can get better so I can have my own adventures, too.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
