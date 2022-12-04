""" 11000060: Betty """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000269$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000272$
        # - $MyPCName$, are you also going to the mainland?
        if pick == 0:
            # $script:0831180407000273$
            # - That's right.
            return 31
        elif pick == 1:
            # $script:0831180407000274$
            # - I don't know.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000275$
            # - You've made a good decision. I've stayed on this small island my whole life, but I want you to go see more of the this world.
            return 31
        elif self.index == 1:
            # $script:0831180407000276$
            # - While you're there at the court, you might as well explore the rest of the mainland. I'd love for you to come back with tales of the things you saw.
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407000277$
        # - Cross the sea to the mainland to experience more of what this world can offer.Go on, don't be afraid.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
