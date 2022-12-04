""" 11000232: George """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000983$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000985$
            # - Dark Wind has changed since $npcName:11000044[gender:0]$ took charge. Now its members are more interested in getting ahead than protecting $map:02000100$ like they used to.
            return 30
        elif self.index == 1:
            # $script:0831180407000986$
            # - And the people of $map:02000100$ are walking on eggshells around them.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
