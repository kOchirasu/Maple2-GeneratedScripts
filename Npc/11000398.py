""" 11000398: Yuna """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001613$
        # - Why did you call me?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001615$
        # - Cough, cough... I'm tired of living in this cesspit. 
        #   I'm going to make it out of here one day! *Cough Cough*
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
