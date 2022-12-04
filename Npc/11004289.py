""" 11004289: Beaumarchais """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0921211107011340$
        # - For such an old hotel, I suppose this place has its charm.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0921211107011341$
        # - My cousin certainly devoted enough time and money to this place. He passed the hotel to me when he died, but I simply have no interest in running it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
