""" 11000485: Mushkid """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002129$
        # - What's up?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002132$
            # - Down below, $npcName:22000321$ has claimed all of the $map:2000202$ for herself!
            return 30
        elif self.index == 1:
            # $script:0831180407002133$
            # - She's bad, but... so cool! I want to be a monster mushroom like her!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
