""" 11000705: Moya """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002837$
        # - What? If you have something to say, say it.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002840$
        # - What? Do you have business with me?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
