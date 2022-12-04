""" 11003824: Strange Claw Marks """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0116111107009757$
        # - <font color="#909090">(There's an odd grouping of large claw marks here.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0116111107009758$
            # - <font color="#909090">(There's an odd grouping of large claw marks here.)</font>
            return 10
        elif self.index == 1:
            # $script:0116111107009759$
            # - <font color="#909090">(This must have been left by a $npcName:11003781[gender:0]$.)</font>
            if pick == 0:
                # $script:0116111107009760$
                # - (Take a picture.)
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:0116111107009761$
        # - <font color="#909090">(This might be a clue. You take a picture of the markings to show them to $npcName:11003536[gender:0]$.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
