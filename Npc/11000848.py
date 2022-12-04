""" 11000848: Phelan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003103$
        # - What is it? I'm doing something really important. Please don't distract me.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003106$
        # - The world keeps changing, and our technology and science leads the way. Mark my words, I'll usher in a new era with my work. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
