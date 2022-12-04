""" 11000099: Caprio """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000388$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000391$
            # - Hey, $MyPCName$! Have you heard about the hero who collected over 1,000 mesos just by hunting monsters? That's me!
            return 30
        elif self.index == 1:
            # $script:0831180407000392$
            # - I think I was born to be a hunter. You should find something that you can be good at and have fun doing.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
