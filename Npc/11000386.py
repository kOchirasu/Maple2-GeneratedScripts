""" 11000386: Hurum """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001571$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001573$
        # - Hello. I am $npcName:11000386$. You seem surprised that I can talk. Don't be. Maple World is full of surprises after all.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
