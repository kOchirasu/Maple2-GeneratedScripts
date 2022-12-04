""" 11000457: Yuri """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002034$
        # - What? Is there something you want to ask me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002037$
        # - It's such a nice day to go for a walk or get some juice, but my dumb lump of a boyfriend wants to stay inside. Look at him, he's not even doing anything! Can you convince him to do something with his life?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
