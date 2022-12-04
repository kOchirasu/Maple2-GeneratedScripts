""" 11003239: Manovich """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008131$
        # - I hope things settle down soon.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008133$
        # - Sigh... What happened to him?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
