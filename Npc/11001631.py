""" 11001631: Bravos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0516130207006133$
        # - Cut to the chase.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0629205207006505$
        # - The moment you step out of here, you're a marked $male:man,female:woman$. Capisce?
        if pick == 0:
            # $script:0629205207006506$
            # - I have no clue what you're talking about.
            return 30
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0629205207006507$
            # - That's fine. You go about your business. You leave the thinking to me.
            return 30
        elif self.index == 1:
            # $script:0630212007006533$
            # - You better be careful. We're watching you.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
