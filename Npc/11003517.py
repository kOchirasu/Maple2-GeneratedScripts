""" 11003517: Ashim """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0817044507008848$
        # - What?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0817044507008851$
        # - What?
        if pick == 0:
            # $script:0817044507008852$
            # - Tell me about the five auras.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0817044507008853$
        # - Aur-what? Look, I just want to finish my exam and grab some grub.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
