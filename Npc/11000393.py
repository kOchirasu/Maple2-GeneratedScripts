""" 11000393: Buffett """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001596$
        # - What seems to be the problem?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407001599$
        # - When my manager is angry, he screams at the top of his lungs and throws anything he can get his hands on. No one can stop him. All you can do is avoid him.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
