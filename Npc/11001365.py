""" 11001365: Dunba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215222907005048$
        # - Sigh... I'm so glad that everyone's safe.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1230171207005755$
        # - I hope the Blackstars leave me alone this time... I don't want a rematch with Vasara Chen...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
