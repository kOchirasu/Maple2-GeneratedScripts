""" 11003957: Thief """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614143707010005$
        # - Eh? You...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614143707010006$
        # - Are you here casing the joint? I've got dibs, alright?!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
