""" 11000118: Cliffine """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000503$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000506$
            # - Usually this place is not so crowded. I didn't expect so many people to be so eager to make money. 
            return 30
        elif self.index == 1:
            # $script:0831180407000507$
            # - $MyPCName$, you looking to scare up some cash too? It's not as dangerous as I expected. Give it a try!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
