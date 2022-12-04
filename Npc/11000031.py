""" 11000031: Asimov """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000181$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000182$
        # - The power of the Green Lapenta is especially strong here in $map:02000023$. That vital force protects this place from darkness.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
