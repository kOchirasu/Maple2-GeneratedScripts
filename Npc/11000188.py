""" 11000188: Rael """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000826$
        # - Cough, cough... Yes?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000828$
        # - I'm still cold... But I have to get better soon. My grandma is worried about me... Cough, cough... 
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407000829$
        # - I wonder what happened to my parents... Cough... I hope they're still out there...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
