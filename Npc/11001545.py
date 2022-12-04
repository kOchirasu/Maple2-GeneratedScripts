""" 11001545: Bravos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0516130207006113$
        # - Ugh. Now what?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0531170907006223$
        # - Hey! You know why they call me $npc:11001545[gender:0]$?
        if pick == 0:
            # $script:0531170907006224$
            # - No clue.
            return 20
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0531170907006225$
            # - 'Cause I'm so great I deserve a standing ovation! Haha! I can't believe you never heard of me. Anyway, you need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
            return 20
        elif self.index == 1:
            # $script:0607145407006336$
            # - Well what're you staring at? Did'ja have something to tell me, or do you just like the view?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.CLOSE
        return Option.NONE
