""" 11004495: Joule  """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012362$
        # - The gravity, erm, situation in this place is fascinating. Why, these huge structures look as though they might simply float away.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012363$
        # - The gravity, erm, situation in this place is fascinating. Why, these huge structures look as though they might simply float away.
        if pick == 0:
            # $script:1227192907012364$
            # - How's the research going?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012365$
            # - It's early to say, but I think this could lead to a second energy revolution.
            return 11
        elif self.index == 1:
            # $script:1227192907012366$
            # - Think about it. The vast majority of Sky Fortress's power generation goes into keeping it in the air. How might we use that power if we had aetherine to lift the ship aloft, instead?
            if pick == 0:
                # $script:0114163707012715$
                # - That would be incredible.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0114163707012716$
        # - And that's why we've got to learn everything we can about aetherine.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
