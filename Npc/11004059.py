""" 11004059: Beatrice """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010091$
        # - The Alemani family will devote all of their resources to aid in the recovery effort.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0614185307010092$
        # - My other half... You have forged a blood oath. I expect you to aid me til the very end.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
