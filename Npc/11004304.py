""" 11004304: Ghost """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1002141907011434$
        # - Can you see me?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1002141907011437$
            # - I guess living people really can see ghosts on Halloween.
            return 30
        elif self.index == 1:
            # $script:1002141907011438$
            # - Please don't ask me if I saw anything...
            if pick == 0:
                # $script:1002141907011439$
                # - Did you see anything?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:1002141907011440$
        # - N-no! I don't want <i>that woman</i> coming after me, so the answer is no!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
