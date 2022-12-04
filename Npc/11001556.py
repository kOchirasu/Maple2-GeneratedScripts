""" 11001556: Laoz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0617105607006360$
        # - Our minds and bodies follow each other in harmony. Consider, the truly wise speak with wisdom, and also act with wisdom.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0727223007006790$
        # - Finally, you have arrived.
        if pick == 0:
            # $script:0727223007006791$
            # - You summoned me?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006792$
            # - Indeed. Your training has brought you to an important crossroad. According to our traditions, it is time for you to set out on a journey to test your skills in the outside world.
            return 40
        elif self.index == 1:
            # $script:0727223007006793$
            # - However, the presence of this terrible darkness must be dealt with first. We can discuss your training later.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
