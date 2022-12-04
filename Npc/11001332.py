""" 11001332: Armachio """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005248$
        # - Ugh...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005251$
        # - Those knuckleheads! Why do they have to fight in here? They'll scare away the customers!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
