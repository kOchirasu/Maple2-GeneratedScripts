""" 11001948: Mrs. O of Middleton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1123165007007494$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1208184307007542$
        # - My darling children are practically virtuosos. That's why I think it's time they learned how to play.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
