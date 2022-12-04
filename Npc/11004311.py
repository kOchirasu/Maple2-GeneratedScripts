""" 11004311: Marianne """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0921211107011348$
        # - I hope I can see papa again soon...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0921211107011349$
        # - You're here! Just like you promised.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
