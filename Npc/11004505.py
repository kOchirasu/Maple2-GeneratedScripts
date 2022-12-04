""" 11004505: Mannstad Sentry """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228182607012429$
        # - Identify yourself!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1228182607012430$
        # - Identify yourself!
        if pick == 0:
            # $script:1228182607012431$
            # - Whoa, there. I'm a friend!
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1228182607012432$
            # - Hey, you're that outlander. I read a report on you.
            return 11
        elif self.index == 1:
            # $script:1228182607012433$
            # - Sorry if I seem on edge. Not all of the outlanders have been as... helpful as you.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.CLOSE
        return Option.NONE
