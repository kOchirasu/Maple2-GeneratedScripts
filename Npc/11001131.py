""" 11001131: Roteo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911192907003866$
        # - Hmm? What do you want?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0911192907003869$
        # - Hah. Cold, are we? Maybe you should've worn thicker clothes.
        if pick == 0:
            # $script:0911192907003870$
            # - I'm not c-c-cold.
            return 31
        elif pick == 1:
            # $script:0911192907003871$
            # - Are you kidding? I'm <b>freezing</b>.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0911192907003872$
        # - Bahaha. A real tough cookie, aren't you?  I'm a professional explorer, and even I get a little cold at times like this. Maybe you belong in my line of work.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0911192907003873$
        # - You look like seasoned adventurer. I'm sure you've seen worse weather than this. So suck it up! Bahaha.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
