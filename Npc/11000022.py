""" 11000022: Harry """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000111$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000114$
        # - Are you heading to $map:02000001$. You know that the way is blocked, right?
        if pick == 0:
            # $script:0831180407000115$
            # - Yeah, I heard.
            return 31
        elif pick == 1:
            # $script:0831180407000116$
            # - No, I didn't. Really?
            return 34
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407000117$
        # - Good, I don't have to explain it to you. So... if you can't get to $map:02000001$, what are you going to do?
        if pick == 0:
            # $script:0831180407000118$
            # - I'll find another way!
            return 32
        elif pick == 1:
            # $script:0831180407000119$
            # - Beats me.
            return 33
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000120$
            # - What are you gonna do, fly? The road is gone! It has ceased to be! You need to be realistic about this.
            return 32
        elif self.index == 1:
            # $script:0831180407000121$
            # - Seriously, have a look at $map:02000115$. Let me know what you think of the terrible, yawning chasm of doom in your way. I'll wait.
            return -1
        return -1

    def __33(self, pick: int) -> int:
        # $script:0831180407000122$
        # - That's understandable. $map:02000001$ has it all, and all we've got is... fish. Might as well head home once you've got your fill of fish, huh?
        return -1

    def __34(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000123$
            # - It sure is. The Royal Road is the main route from this harbor to $map:02000001$, and it was cracked open by the earthquake that happened the other day. Now no one can get to $map:02000001$.
            return 34
        elif self.index == 1:
            # $script:0831180407000124$
            # - If you don't believe me, go to $map:02000115$ and see for yourself.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.NEXT
        elif (self.state, self.index) == (34, 1):
            return Option.CLOSE
        return Option.NONE
