""" 11004055: Oska """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010083$
        # - The siege on Madrakan was successful, but it cost us a great deal.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0614185307010084$
        # - The siege on Madrakan was successful, but it cost us a great deal.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
