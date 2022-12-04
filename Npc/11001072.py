""" 11001072: Brave Tree Spirit """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003655$
        # - Go away.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003658$
        # - You're from the outside world, aren't you? What are you going to change here this time?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
