""" 11000170: Leta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000710$
        # - What seems to be the problem?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000712$
        # - $npcName:11000174[gender:1]$ and I grew up together in the same neighborhood. I started to notice my heart racing and my mood brightening whenever I thought about $npcName:11000174[gender:1]$. I've honestly never felt like this about anyone else before.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407000713$
        # - $npcName:11000174[gender:1]$ and I grew up together in the same neighborhood. I started to notice my heart racing and my mood brightening whenever I thought about $npcName:11000174[gender:1]$. I've honestly never felt like this about anyone else before.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0317164707008110$
        # - How may I help you?
        if pick == 0:
            # $script:0317164707008111$
            # - Have you seen anyone in a mask go through here?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0317164707008112$
        # - I sure did! Hard not to notice someone that odd. He ran off toward the Kerning Interchange.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
