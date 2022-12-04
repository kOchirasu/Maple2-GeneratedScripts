""" 11000442: Cathy Mart Employee """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001859$
        # - Can I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001861$
        # - I don't want to talk. I got ripped off by my boss, and then I almost got killed by robbers. My life sucks!
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407001862$
        # - Do you want to know what the owner of Cathy Mart is like? The worst, that's what! 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
