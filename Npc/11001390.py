""" 11001390: Yul """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005390$
        # - Sigh...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1223165107005568$
        # - My daughter, $npcName:11001396[gender:1]$, is always lost in thought. What could keep her so preoccupied all day long?
        if pick == 0:
            # $script:1226235907005589$
            # - Tell me about her.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:1223165107005569$
            # - She used to be such a clever girl. Even the people in $map:02010002$ heard about her genius.
            return 31
        elif self.index == 1:
            # $script:1223165107005570$
            # - But instead of going out and making something of herself, she came back to this small town. I'm happy to have her here, but I can't help but feel that she's wasting her talent...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        return Option.NONE
