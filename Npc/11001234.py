""" 11001234: Ryder """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1125194807004482$
        # - Have you seen anyone out of place?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1125194807004485$
        # - $npc:11001231[gender:0]$ hurt dozens of us when he escaped last night. We all knew we didn't stand a chance, but what else could we do? I'm in no shape to help bring him in, but at least I can keep a lookout.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
