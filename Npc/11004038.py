""" 11004038: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010061$
        # - Ah, you're here. It's thanks to you that we were all able to find common ground and work as one. Terrun Calibre will do whatever it can to help you with the matter of Madrakan.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614185307010062$
        # - Ah, you're here. It's thanks to you that we were all able to find common ground and work as one. Terrun Calibre will do whatever it can to help you with the matter of Madrakan.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
