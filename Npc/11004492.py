""" 11004492: Pantanal """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012337$
        # - Ah, $MyPCName$! I'm here researching the plants of Kritias.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012338$
        # - Ah, $MyPCName$! I'm here researching the plants of Kritias.
        if pick == 0:
            # $script:1227192907012339$
            # - What have you learned?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012340$
            # - So much! All of the plants in Kritias have at least a little bit of aetherine in them.
            return 11
        elif self.index == 1:
            # $script:1227192907012341$
            # - And the plants react to each other's aetherine. It seems like they use the aetherine to communicate with each other!
            if pick == 0:
                # $script:1227192907012342$
                # - So what... talking plants?
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012343$
            # - Not precisely, but the idea of plants being able to communicate with each other isn't exactly new. The ecosystem in Kritias may be the most concrete evidence we've ever seen.
            return 12
        elif self.index == 1:
            # $script:1227192907012344$
            # - The plants are all giving off the same aetherine wavelength. It's almost as if they're singing a chorus!
            if pick == 0:
                # $script:0114164007012721$
                # - Incredible!
                return 13
            return -1
        return -1

    def __13(self, pick: int) -> int:
        # $script:0114164007012722$
        # - Astonishing, too!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        return Option.NONE
