""" 11004207: Koomkoom """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0803202415009087$
        # - Heheh, want to play with me?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0803202415009088$
        # - Heheheh... I've got something real fun cooked up for those humans. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
