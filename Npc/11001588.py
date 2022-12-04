""" 11001588: Rejan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006076$
        # - I miss Calibre... 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006127$
        # - Can we ever go back to Calibre Island?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
