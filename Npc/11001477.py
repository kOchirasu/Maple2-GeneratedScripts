""" 11001477: Blackstar Gangster """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228113207005717$
        # - What brings you here?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1228113207005719$
        # - Those weren't ordinary train robbers.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
