""" 11000462: Amelia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002052$
        # - How may I help you?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002056$
        # - What brings you to $map:02000107$? Since you're here, I was thinking about changing up my skin tone again. Do you think I should do it?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
