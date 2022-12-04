""" 11000266: Jin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001085$
        # - What brings you here?
        return None # TODO

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001087$
            # - Captain $npcName:11000044[gender:0]$ commands Dark Wind now, but before the Blue Lapenta broke we were led by Winn Stilton. Every member of Dark Wind, myself included, considered Captain Stilton a true hero.
            return 20
        elif self.index == 1:
            # $script:0831180407001088$
            # - That's why we can never forgive $npcName:11000064[gender:0]$! He not only destroyed the Blue Lapenta, but he also killed Captain Stilton!
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407001089$
        # - I can't believe $npcName:11000044[gender:0]$ ended Captain Stilton's life. That brazen coward fooled us all!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
