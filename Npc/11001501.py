""" 11001501: Dunba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0118150907005840$
        # - You know I outrank you, right? Hah hah!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0118150907005843$
        # - Don't just stare at your food, eat it! So rude.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
