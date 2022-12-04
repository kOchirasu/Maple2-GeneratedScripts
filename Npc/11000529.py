""" 11000529: Blackeye """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002267$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002270$
        # - Dark Wind has changed too much. Now it's crushing the citizens under authoritarian rule instead of protecting them like they used to. I can't let this continue.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407002271$
        # - $MyPCName$, do the people in this city look happy to you?
        if pick == 0:
            # $script:0831180407002272$
            # - Yep!
            return 41
        elif pick == 1:
            # $script:0831180407002273$
            # - Beats me.
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002274$
        # - Then you're a fool. There's no point in discussing this further. Leave.
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180407002275$
        # - Try to see through their deceptions. It's not hard to find the rotting heart of this city.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
