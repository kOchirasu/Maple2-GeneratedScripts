""" 11000208: Nick """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000892$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000894$
            # - There's been plenty of talk about Captain $npcName:11000044[gender:0]$'s leadership in Dark Wind, but I like his style. He said he'd evaluate every member based on their skill and performance. That's fair and reasonable.
            return 20
        elif self.index == 1:
            # $script:0831180407000895$
            # - Those who have problems with it clearly just aren't good enough.
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407000896$
        # - Follow this road southward to find the Barrota Trading Company's warehouse at the end. Start your search there, and you should find $item:20000046$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
