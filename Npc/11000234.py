""" 11000234: Cindy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000993$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000995$
        # - Did you come from the rich neighborhood? What are you doing here?
        if pick == 0:
            # $script:0831180407000996$
            # - Do you know $npcName:11000064[gender:0]$?
            return 21
        return -1

    def __21(self, pick: int) -> int:
        # $script:0831180407000997$
        # - $npcName:11000064[gender:0]$? Who's that? Is he famous?
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000998$
            # - The people living in the rich neighborhood think we're smelly and dirty. But Mr. $npcName:11000006[gender:0]$ said they're smellier and dirtier on the inside for thinking that.
            return 30
        elif self.index == 1:
            # $script:0831180407000999$
            # - Mr. $npcName:11000006[gender:0]$ said he'd change the world, so everyone could be equal and happy together.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
