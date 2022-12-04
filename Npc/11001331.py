""" 11001331: Mrs. Arthur """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005244$
        # - Oww...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005247$
        # - One moment, I'm shopping on cloud nine. The next moment... I don't know if I ever want to go shopping again!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
