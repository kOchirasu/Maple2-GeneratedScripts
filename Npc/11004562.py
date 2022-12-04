""" 11004562: Rolling Thunder """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0220211107014515$
        # - Hey!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0220211107014516$
        # - Ha! I should've known you'd be here. Someone like you can't resist a good rumble.
        if pick == 0:
            # $script:0220211107014517$
            # - You've got me there.
            return 20
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014518$
            # - That's the $MyPCName$ I remember! Hold on... This means we might have to fight each other.
            return 20
        elif self.index == 1:
            # $script:0220211107014519$
            # - Well, well. Now I've got some real competition! Let's do our best, okay?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.CLOSE
        return Option.NONE
