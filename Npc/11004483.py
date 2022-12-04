""" 11004483: Cabomba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012249$
        # - Hello! I'll be helping you explore Kritias. Nice to meet you.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012250$
        # - Hello! I'll be helping you explore Kritias. Nice to meet you.
        if pick == 0:
            # $script:1227192907012251$
            # - When do you start?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012252$
            # - St-st-st-start? Soon! Really soon! Yeah...
            return 11
        elif self.index == 1:
            # $script:1227192907012253$
            # - There's lots and lots of preparation to do. So that's what I'm doing... Preparing! Yep. Gotta prepare before you can go out into the wilderness...
            if pick == 0:
                # $script:1227192907012254$
                # - It's okay to be scared.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:1227192907012255$
        # - I'm not scared! I'm c-cautious, okay? This is an important j-j-j-job. I'm <i>definitely</i> not stalling!
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
