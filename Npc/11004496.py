""" 11004496: Denison """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012369$
        # - Ah! You're that $male:fellow,female:lady$, from Sky Fortress. Are you here to ask about my research?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012370$
        # - Ah! You're that $male:fellow,female:lady$, from Sky Fortress. Are you here to ask about my research?
        if pick == 0:
            # $script:1227192907012371$
            # - Sure. Tell me about it.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012372$
            # - Since we arrived in Kritias, I've been looking into the connection between the local wildlife and this miraculous "aetherine" substance.
            return 11
        elif self.index == 1:
            # $script:1227192907012373$
            # - No matter how big or small, every creature I've sampled has some amount of aetherine in it.
            if pick == 0:
                # $script:0114164607012726$
                # - Ah, yes. Fascinating.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0114164607012727$
        # - Is there some connection between aetherine and life energy? I'll have to do more science to know for sure.
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
