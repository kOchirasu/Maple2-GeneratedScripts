""" 11003534: Condor """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1126150707011919$
        # - Back in my day, we knew a thing or two about duty!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1126150707011920$
        # - What's the matter? Don't have enough to do?
        if pick == 0:
            # $script:1126150707011921$
            # - Uh...
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1126150707011922$
        # - If you've got time for chit-chat, you've got time for a mission!
        return -1

    def __40(self, pick: int) -> int:
        # $script:1126150707011923$
        # - If you think you've got what it takes to serve the Imperial Vanguard, then prove it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
