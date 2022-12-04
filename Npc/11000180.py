""" 11000180: Konus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000743$
        # - What?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000746$
        # - That stuff you're carrying don't look like junk. Are you going to toss it? People nowadays throw out just any old thing. New, old, doesn't matter. I found boxes of stuff like that. 
        if pick == 0:
            # $script:0831180407000747$
            # - What kinds of things did you find?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000748$
            # - Ha! Everything, my friend. Sometimes little baubles, sometimes official palace weapons. Found a lot of those lately, ever since the empress's court was canceled.
            return 31
        elif self.index == 1:
            # $script:0831180407000749$
            # - A lot of time and effort went into making those weapons. Why not stockpile them? They'd be more useful than melting them down, surely.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        return Option.NONE
