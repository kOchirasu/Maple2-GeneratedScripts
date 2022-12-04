""" 11000511: Elliana Shuabritze """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000580$
        # - What do you want?
        return None # TODO

    def __10(self, pick: int) -> int:
        # functionID=1 
        # $script:0624180010002188$
        # - Do you have old enchanted equipment you don't need anymore? I'll turn it into a scroll so you can transfer the enchantment to your new gear!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
