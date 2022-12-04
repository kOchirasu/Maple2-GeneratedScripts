""" 11004493: Bacopa """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012347$
        # - I'm here researching the fish of Kritias.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012348$
        # - I'm here researching the fish of Kritias.
        if pick == 0:
            # $script:1227192907012349$
            # - What have you learned?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012350$
            # - Every fish I've caught has had trace amounts of aetherine in their systems. The amount might be related to their place in the food chain...
            return 11
        elif self.index == 1:
            # $script:1227192907012351$
            # - If I were to cook and eat one of these fish, would the aetherine stay in <i>my</i> system? Until I figure this out, we're going to be reliant on food rations delivered from the mainland.
            if pick == 0:
                # $script:0114161207012703$
                # - I hope you figure it out.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0114161207012704$
        # - So do I, my friend. So do I.
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
