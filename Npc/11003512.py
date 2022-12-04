""" 11003512: Babatundey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0817044507008802$
        # - Need something?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0817044507008803$
        # - The boss's word is good. What more do you need?
        if pick == 0:
            # $script:0817044507008804$
            # - Tell me about the exam.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0817044507008805$
        # - Humans can't do anything alone. If you can't figure it out, ask someone to help you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
