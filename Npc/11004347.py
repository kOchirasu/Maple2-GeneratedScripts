""" 11004347: Mia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011751$
        # - I must remain calm... I can resolve this... All things in their proper place...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011752$
        # - If there's a problem, solve it! Blaming and complaining won't fix anything!
        if pick == 0:
            # $script:1109213607011753$
            # - Things aren't looking so good right now... are you okay?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109213607011754$
        # - Yes, of course! Obviously we just need to remain calm and composed. CALM AND COMPOSED!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
