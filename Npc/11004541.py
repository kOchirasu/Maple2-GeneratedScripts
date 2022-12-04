""" 11004541: Nuel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0110183907012675$
        # - Ugh... I hate deadlines...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0110183907012676$
            # - Ugh... I hate deadlines...
            return 10
        elif self.index == 1:
            # $script:0110183907012677$
            # - Here to gawk at the soldierettos? Get a good look and then be on your way. I can't concentrate with all you... all you tourists hanging about!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
