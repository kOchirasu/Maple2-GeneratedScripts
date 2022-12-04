""" 11004509: Mannstad Sentry """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228182607012451$
        # - Look what we have here. It's about time they sent us some reinforcements.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1228182607012452$
        # - Look what we have here. It's about time they sent us some reinforcements.
        if pick == 0:
            # $script:1228182607012453$
            # - I'm not your reinforcements.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1228182607012454$
        # - Tch... Figures. We don't have the numbers to hold this position for right now. Y'know, give a leshy a gun and I'd let it stand guard. That's how desperate we are!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
