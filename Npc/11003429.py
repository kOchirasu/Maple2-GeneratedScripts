""" 11003429: Silver Wolf """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0719173007008675$
        # - I sense the war chief at the top of the hourglass. And yet... something is amiss.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0719173007008676$
        # - I sense the war chief at the top of the hourglass. And yet... something is amiss.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
