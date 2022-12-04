""" 11000301: Jax """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001194$
        # - What brings you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001196$
        # - This place is dangerous. Be careful, especially if you want to use skills while on the Bone Bridge. Things can get scary there pretty quickly.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
