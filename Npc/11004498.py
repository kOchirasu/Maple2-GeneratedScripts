""" 11004498: Lyton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012384$
        # - Who's there? Oh, you're that... that $MyPCName$ hero!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012385$
        # - Who's there? Oh, you're that... that $MyPCName$ hero!
        if pick == 0:
            # $script:1227192907012386$
            # - What are you doing here?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012387$
            # - I'm the foremost cultural anthropologist of Sky Fortress, here to study the cultures of Kritias. And I feel I've already made a great discovery!
            return 11
        elif self.index == 1:
            # $script:1227192907012388$
            # - I've uncovered some ancient writings here, and the motifs and archetypes on display are similar to those in ancient Victoria Island literature. Uncannily so.
            if pick == 0:
                # $script:1227192907012389$
                # - That seems a little unlikely.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:1227192907012390$
        # - It begs the question: do our cultures share the same root? Of course, the higher-ups will only accept evidence that our culture came first, and that Kritias copied us...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
