""" 11001949: Mochar """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1123165007007495$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1208184307007545$
        # - But I don't <i>want</i> to be a musician! 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
