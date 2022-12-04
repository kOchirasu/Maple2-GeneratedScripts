""" 11000629: Kimo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002530$
        # - Screeeeech!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002532$
        # - $map:02000051$ is a great place to raise a family like mine. Its highlands are safe from monsters on the ground, and my children can practice flying!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
