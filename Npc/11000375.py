""" 11000375: Luvar """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001541$
        # - What seems to be the problem?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001543$
        # - Enoki mushrooms grow here. They require clean, undisturbed areas to flourish. I suppose no one ever comes to this valley, then.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
