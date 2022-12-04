""" 11000842: Angela """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003080$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003083$
        # - Ah, I don't care about justice or world peace. I just don't like it when people bully the weak. No one has the right to make others suffer, no matter how strong they are. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
