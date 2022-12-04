""" 11000257: Douglas """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000408$
        # - How may I help you?
        return None # TODO

    def __1(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180610000413$
        # - Being strong is important, but looking fabulous while you fight is the true key to happiness, y'know. So... wanna spruce up your gear?
        if pick == 0:
            # $script:0831180610000414$
            # - Yes! I need more color in my life!
            return 0
        return None # TODO

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.SELECTABLE_BEAUTY
        return Option.NONE
