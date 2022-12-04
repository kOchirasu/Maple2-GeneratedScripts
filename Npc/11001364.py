""" 11001364: Tara """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215222907005047$
        # - All of us here, together... It reminds me of the old days.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1230171207005754$
        # - Okay, I admit it. You're a good person. I can't always be right, you know. Anyway, thank you for the help.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
