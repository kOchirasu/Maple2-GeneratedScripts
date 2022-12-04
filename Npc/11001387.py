""" 11001387: Krata """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005387$
        # - I'm tired. Really tired!
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1223165107005549$
            # - I've been getting terrible joint pain lately. Normally that'd mean there's a storm brewing, but it doesn't rain here. Very strange.
            return 40
        elif self.index == 1:
            # $script:1223165107005550$
            # - There's a rumor that all the ailments that have struck the town lately are from an ancient curse.
            if pick == 0:
                # $script:1223165107005551$
                # - What kind of curse?
                return 41
            return -1
        return -1

    def __41(self, pick: int) -> int:
        # $script:1223165107005552$
        # - Never mind. I shouldn't have mentioned it to an outsider in the first place. If you'll excuse me, I need to gather herbs for my arthritis.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
