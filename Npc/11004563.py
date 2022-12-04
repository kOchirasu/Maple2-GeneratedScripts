""" 11004563: Allon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0220211107014520$
        # - Hm?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014521$
            # - Hm?
            return 10
        elif self.index == 1:
            # $script:0220211107014522$
            # - I had a feeling I'd see you here.
            if pick == 0:
                # $script:0220211107014523$
                # - I didn't think you were into this kind of thing.
                return 20
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014524$
            # - Come now. I wouldn't pass up the chance to fight the hero of Tria.
            return 20
        elif self.index == 1:
            # $script:0220211107014525$
            # - I look forward to our match.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.CLOSE
        return Option.NONE
