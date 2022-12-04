""" 11000977: Kunbasha """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003379$
        # - What's a human doing in a place like this?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003381$
        # - Only we kunkun can feel the flow of nature and foretell the weather. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
