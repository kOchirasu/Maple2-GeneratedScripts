""" 11001336: Bodis """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005263$
        # - Someday we'll have a customer who returns their board...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005266$
        # - Back in my day, we'd explore the whole world on our skateboards. I even shredded over the hot desert sands... Ah, those were good times.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
