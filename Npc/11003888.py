""" 11003888: Celine """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515102507009930$
        # - Listen closely to the waves. Can you hear the voice of the ocean?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0515102507009931$
        # - Listen closely to the waves. Can you hear the voice of the ocean?
        return -1

    def __30(self, pick: int) -> int:
        # $script:0515102507009932$
        # - I'm sure you can quiet the angry seas.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
