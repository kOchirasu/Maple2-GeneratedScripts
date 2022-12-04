""" 11003421: Evagor """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0706160807008629$
        # - Don't waste my time. $map:02000051$ doesn't need the likes of you.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0706160807008630$
        # - You want to stay here? You gotta take the warrior's test.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
