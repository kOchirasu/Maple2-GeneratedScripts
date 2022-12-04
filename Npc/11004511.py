""" 11004511: Mannstad Patrolman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228182607012461$
        # - Ugh... I'm ready to pass out on my feet...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1228182607012462$
            # - Ugh... I'm ready to pass out on my feet...
            return 10
        elif self.index == 1:
            # $script:1228182607012463$
            # - AAAAH! Ugh, you startled me.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
