""" 11000987: Horok """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003401$
        # - Hey, how did you find this place?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003403$
        # - It's coming, and we don't have much time left. We must find shelter quickly. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
