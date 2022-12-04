""" 11001130: Nordan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911192907003858$
        # - D-do you want some herbs?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0911192907003861$
        # - W-what's with those weird noises? You hear them too, r-right?
        if pick == 0:
            # $script:0911192907003862$
            # - I didn't hear anything.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0911192907003863$
        # - What?! D-don't look at me like that... I'm not crazy!
        if pick == 0:
            # $script:0911192907003864$
            # - It was probably just a small animal.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0911192907003865$
        # - Y-you think so? You'll protect me if it's something scary though, right? Hngg... Now my heart is p-pounding.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
