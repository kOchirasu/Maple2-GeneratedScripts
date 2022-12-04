""" 11003140: Jorge """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0222124707007951$
        # - What brings you here?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0224093607007961$
        # - Don't you just love the smell of my garden? My greatest joy is when I manage to reproduce extinct medicinal flowers. Heh... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
