""" 11000340: Zobek """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001360$
        # - What can I do for you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001363$
        # - I've been by $npcName:11000341[gender:1]$'s side since she was born. It's the least I could do to repay her grandfather, who took me under his wing when I had no place to go.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407001364$
        # - If the Andreas hadn't fallen so easily, this $map:02000178$ would not be here today. 
        if pick == 0:
            # $script:0831180407001365$
            # - What happened to the Andreas?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407001366$
        # - T-that's... Ah, let's not stir up old, painful memories.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
