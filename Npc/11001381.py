""" 11001381: Modir """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217192807005381$
        # - Hm? What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1228164407005724$
        # - I'm thinking up ways to bring prosperity to $map:02010036$. If you want to chat, talk to someone else.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
