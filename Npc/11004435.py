""" 11004435: Condor """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1213154907011974$
        # - Back in my day, we knew a thing or two about duty!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1213154907011975$
        # - Don't look so glum, Cadet. We're in a new land full of new and exciting things to eat!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
