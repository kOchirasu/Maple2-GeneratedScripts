""" 11000431: Ronin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 41])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001797$
        # - I'd better rest while I can!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001799$
        # - I've heard stories of treasure chests under the sea, but I've never seen one. How about you, $MyPCName$?
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407001800$
        # - Yes?
        if pick == 0:
            # $script:0831180407001801$
            # - $npcName:11000362[gender:0]$'s special...
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407001802$
        # - Go away.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
