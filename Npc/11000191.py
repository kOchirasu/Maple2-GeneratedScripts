""" 11000191: Mrs. Hofmann """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000858$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000861$
        # - I think my husband should've married his job instead of me. He's never home.
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000862$
            # - I used to love the aroma of herbs that followed my husband, but that was before we married. He's so obsessed with them now that he never has time to help around the house.
            return 30
        elif self.index == 1:
            # $script:0831180407000863$
            # - Sometimes I wonder... I wonder if I should take the kids to $map:02000002$ for a fresh start. There's more to being a good husband than just putting food on the table. 
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
