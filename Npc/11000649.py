""" 11000649: Prisoner 170121 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002656$
        # - What are you looking at?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002660$
        # - Another tourist? Come to see all the animals in their cages?
        if pick == 0:
            # $script:0831180407002661$
            # - How did you end up in here?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002662$
        # - I swore, and apparently that's SO wrong that they had to throw me into prison?
        return -1

    def __50(self, pick: int) -> int:
        # $script:1211023307004934$
        # - Another tourist? Come to see all the animals in their cages?
        if pick == 0:
            # $script:1211023307004935$
            # - Do you know someone named $npcName:11001231[gender:0]$?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1211023307004936$
        # - No. Get lost.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        return Option.NONE
