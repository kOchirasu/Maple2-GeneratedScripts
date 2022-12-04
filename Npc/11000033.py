""" 11000033: Jorge """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000185$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000188$
        # - Ancient tomes containing stories of this world must be handled with care. They can teach us many important lessons.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0530154307008539$
        # - Are you lost? Why are you bothering me?
        if pick == 0:
            # $script:0530154307008540$
            # - Take me to $map:52000133$.
            return 41
        elif pick == 1:
            # $script:0530154307008541$
            # - Just thought I'd pay you a social visit.
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # functionID=1 
        # $script:0530154307008542$
        # - $npcName:11000031[gender:0]$ says you're all right, so fine. Off you go.
        return -1

    def __42(self, pick: int) -> int:
        # $script:0530154307008543$
        # - All right, then. I hope you're enjoying $map:02000023$.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0530154307008544$
        # - The ancient records of our history must be handled with care. They teach us many important lessons.
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
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
