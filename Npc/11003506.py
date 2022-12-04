""" 11003506: Seren """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115009005$
        # - Do you need more candy packs?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115009006$
        # - Ever since those hungry $itemPlural:61000002$ showed up, this place has been overflowing with tourists. I actually ran into a childhood friend the other day!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
