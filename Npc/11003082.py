""" 11003082: Chorrie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0113143107007764$
        # - Sniff, sniff... Chorrie is scared... Too many evil people out there.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0113143107007767$
        # - No, no. Don't. I don't know anything. I really don't.
        if pick == 0:
            # $script:0113143107007768$
            # - Aww, it's okay. Take it easy.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0113143107007769$
        # - Sob... No one knows how I feel. Why can't I be left alone? Sob...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
