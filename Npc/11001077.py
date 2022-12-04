""" 11001077: Tantamomi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003675$
        # - A full moon... The Kakas... Aw, please help me. Hah hah, hah hah hah!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003678$
        # - D-don't come near me. No! I need a friend. No, no... L-let's start again... Ha!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
