""" 11000265: Bordeaux """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001082$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001084$
        # - The secrets of the Land of Darkness and Shadow Word cannot be explained by logic. Nature was not created by mathematics or science. They have a life all their own, which must be understood. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
