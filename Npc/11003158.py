""" 11003158: Carly """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0306155707008054$
        # - Can I help you?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0306155707008058$
        # - This is my favorite place. It's beautiful and smells even better. And, you might not know this, but I can also eat delicious food here!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
