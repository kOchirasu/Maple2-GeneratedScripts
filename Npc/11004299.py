""" 11004299: Ghost """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1002141907011387$
        # - Everything in its place. 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1002141907011390$
        # - A guest came the other day, but I haven't seen him lately. I do hope he's having a nice visit.
        if pick == 0:
            # $script:1002141907011391$
            # - Who are you talking about?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1002141907011392$
        # - A gentleman with a large briefcase. None of the other ghosts recognized him, but it seems that he was an acquaintance of mademoiselle.
        if pick == 0:
            # $script:1002141907011393$
            # - Mademoiselle?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1002141907011394$
        # - Yes, the lady of the hotel. There were evil thoughts in her mind when she met the gentleman. A ghost has a sixth sense about these things, you know.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
